import os
import re

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()

        # Update text colors
        content = re.sub(r'color:\s*white;', 'color: #36454F;', content)
        content = re.sub(r'color:\s*rgb\(255,\s*255,\s*255\);', 'color: #36454F;', content)

        # Update navbar background color specifically
        # We find the .navbar block and replace background-color inside it
        
        # In index.html, it's currently #FFFDD0, in others it might be #17223a
        def navbar_replacer(match):
            block = match.group(0)
            block = re.sub(r'background-color:\s*(#[0-9a-fA-F]+|darkblue|#FFFDD0|#17223a);', 'background-color: #EAE6B8;', block)
            return block

        content = re.sub(r'\.navbar\s*\{[^}]*\}', navbar_replacer, content)

        with open(filepath, 'w') as f:
            f.write(content)

print("Colors updated successfully.")
