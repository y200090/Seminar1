# ===============正規表現 11/10===============

import csv

filename = 'dummy.csv'
with open(filename, 'r', encoding='utf-8') as f:
    dummy_data = csv.reader(f)
    # 先頭行を飛ばす
    next(dummy_data)

    string_data = []
    for row in dummy_data:
        string_data.append(' '.join(row))

    # string_data = ''
    # for row in dummy_data:
    #     string_data += ' '.join(row)
    #     string_data += '\n'
    # string_data = string_data.rstrip()

import re

# メールアドレスのパターン
pattern = '[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+'
repattern = re.compile(pattern)

for sdata in string_data:
    result = repattern.search(sdata)
    if result:
        print('Match String: ' + '\033[35m' + f'{result.group()}' + '\033[0m')
    else:
        print(f'Match String: None')

# result = repattern.findall(string_data)
# for target in result:
#     print(target)
