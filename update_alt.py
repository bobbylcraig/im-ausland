import os
import re

posts_dir = '_posts'
for filename in os.listdir(posts_dir):
    if not filename.endswith('.md'):
        continue
    filepath = os.path.join(posts_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    
    def replacer(match):
        img_tag = match.group(0)
        if 'alt=' in img_tag:
            return img_tag
        src_match = re.search(r'src="[^"]*/([^/"]+)-min\.jpg"', img_tag)
        if src_match:
            basename = src_match.group(1)
            alt_text = basename.replace('-', ' ').title()
            return img_tag.replace('>', f' alt="{alt_text}">')
        return img_tag

    new_content = re.sub(r'<img[^>]*>', replacer, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)

print("Updated images.")
