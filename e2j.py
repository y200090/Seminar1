# ===============辞書課題 11/24===============
# 英日辞書引きプログラム

import csv, re

with open('data/ej_sys.tsv', 'r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter='\t')

    content = ''
    for line in data:
        content += '\t'.join(line) + '\n'

while True:
    words = input('input English words (end with Enter): ')
    if words == '':
        print('>>> プログラムを終了します。')
        break

    # パターンマッチした部分(r'\1')に'\'を追加してエスケープを行う
    words = re.sub('([/\-.+*?^$({)}|])', r'\\\1', words)

    print('--------------------')
    
    result = None
    for result in re.finditer(f'^{words}\t.\t(.*)', content, re.MULTILINE):
        print(result.group(1))

    # パターンマッチしなかった場合
    if result is None:
        print(result)
    
    print('--------------------\n')
