# ===============辞書課題 11/24===============
# 日英辞書引きプログラム

import csv, re

with open('data/je_sys.tsv', 'r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter='\t')
    content = ''
    for line in data:
        content += '\t'.join(line) + '\n'

while True:
    word = input('input a Japanese word (end with Enter): ')
    if word == '':
        print('>>> プログラムを終了します。')
        break
        
    print('--------------------')

    results = re.finditer(f'^{word}\t.\t(.*)', content, re.MULTILINE)
    result = None
    for result in results:
        print(result.group(1))
        
    # パターンマッチしなかった場合
    if result is None:
        print(result)

    print('--------------------\n')
