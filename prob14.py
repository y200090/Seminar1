# ===============課題14 11/17===============

import re

with open('data/14.dat', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile('([a-zA-Z]+):(\d+)')
result = dict(pattern.findall(content))
for key, value in result.items():
    print(key, value)

avg = sum(list(map(int, result.values()))) / len(result)
print(f'avg: {avg}')
