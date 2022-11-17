# ===============辞書課題 11/24===============
# 日英辞書引きプログラム

import csv, re

with open('data/je_sys.tsv', 'r', encoding='utf-8') as f:
    # data = csv.reader(f, delimiter='\t')
    # content = ''
    # for line in data:
    #     content += '\t'.join(line) + '\n'

    # data = [line.split('\t') for line in f]
    # content = ''
    # for line in data:
    #     content += '\t'.join(line) + '\n'

    content = f.read()

while True:
    word = input('input a Japanese word (end with Enter): ')
    if word == '':
        print('>>> プログラムを終了します。')
        break
        
    results = re.finditer(f'{word}\t.\t(.*)', content, re.MULTILINE)

    print('--------------------')

    result = None
    for result in results:
        print(result.group(1))

    if result is None:
        print('Not Found')

    print('--------------------\n')
