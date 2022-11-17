# ===============課題14 11/17===============

import re

with open('assets/14.dat', 'r', encoding='utf-8') as f:
    content = f.read()

result = dict(re.findall('([a-zA-Z]+):(\d+)', content))

for key, value in result.items():
    print(key, value)

# 平均値
avg = sum(list(map(int, result.values()))) / len(result)
print(f'avg: {avg}')
