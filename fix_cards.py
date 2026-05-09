import re

with open('projects.html', 'r') as f:
    content = f.read()

fund_types = ['Funds to Support Product', 'Funds to Support Founder']
idx = [0]

def replace_button(match):
    fund = fund_types[idx[0] % 2]
    idx[0] += 1
    return (
        f'<p class="card-meta">[Author]</p>\n'
        f'                    <p class="fund-type">{fund}</p>\n'
        f'                    <div class="card-actions">\n'
        f'                        <button><a href="#">View</a></button>\n'
        f'                        <button class="donate-btn"><a href="#">Donate</a></button>\n'
        f'                    </div>'
    )

# Only target the standalone <button><a href="#">View</a></button> inside project cards
content = re.sub(r'<button><a href="#">View</a></button>', replace_button, content)

with open('projects.html', 'w') as f:
    f.write(content)

print(f"Replaced {idx[0]} View buttons.")
