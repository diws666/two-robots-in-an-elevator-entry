import os

LINE = "So... do you come up here often, or do you just enjoy standing between floors with a stranger who has no small talk installed?"  # verified count: 126 chars

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
