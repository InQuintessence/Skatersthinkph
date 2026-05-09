import os
import re

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()

        # Fix the bad background-color replacement that happened before
        content = re.sub(r'background-color:\s*#36454F;', 'background-color: white;', content)

        # Specifically replace color: white and rgb(255, 255, 255) for index.html which was missed
        # But we must be careful not to match background-color.
        # Negative lookbehind: (?<!-)color: white;
        
        content = re.sub(r'(?<!-)color:\s*white;', 'color: #36454F;', content)
        content = re.sub(r'(?<!-)color:\s*rgb\(255,\s*255,\s*255\);', 'color: #36454F;', content)
        content = re.sub(r'(?<!-)color:\s*#FFFDD0;', 'color: #36454F;', content)

        with open(filepath, 'w') as f:
            f.write(content)

print("Colors fixed successfully.")
