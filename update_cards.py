import re

with open('projects.html', 'r') as f:
    content = f.read()

# 1. Add CSS for card-meta, fund-type, card-actions, donate-btn after .project-card button a
css_addition = '''
        .card-meta {
            font-size: 13px;
            color: #36454F;
            opacity: 0.75;
            margin-bottom: 4px;
            font-style: italic;
        }

        .fund-type {
            font-size: 13px;
            font-weight: bold;
            color: #36454F;
            margin-bottom: 10px;
        }

        .card-actions {
            display: flex;
            gap: 8px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .project-card button.donate-btn {
            background-color: #e11d48;
        }'''

# Insert after .project-card button a block
content = content.replace(
    '        .carousel-nav {',
    css_addition + '\n\n        .carousel-nav {'
)

# Fund type cycle — alternate per card: Product, Founder, Product, Founder ...
fund_types = ['Funds to Support Product', 'Funds to Support Founder']
card_count = [0]  # mutable counter

def replace_card(match):
    inner = match.group(1)
    idx = card_count[0]
    card_count[0] += 1
    fund = fund_types[idx % 2]
    
    # Replace the single <button><a href="#">View</a></button> with meta + fund + actions
    inner = re.sub(
        r'(\s+)<button><a href="#">View</a></button>',
        lambda m: (
            f'\n                    <p class="card-meta">[Author]</p>'
            f'\n                    <p class="fund-type">{fund}</p>'
            f'\n                    <div class="card-actions">'
            f'\n                        <button><a href="#">View</a></button>'
            f'\n                        <button class="donate-btn"><a href="#">Donate</a></button>'
            f'\n                    </div>'
        ),
        inner,
        count=1
    )
    return f'<div class="project-card">{inner}</div>'

content = re.sub(
    r'<div class="project-card">(.*?)</div>',
    replace_card,
    content,
    flags=re.DOTALL
)

with open('projects.html', 'w') as f:
    f.write(content)

print(f"Done. Updated {card_count[0]} cards.")
