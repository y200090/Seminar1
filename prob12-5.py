# ===============課題12 11/10===============

import re

# 文字列が英文字のみで構成されているパターン
pattern = '[a-zA-Z]+'
repattern = re.compile(pattern)

while True:
    content = input('>>> ')

    if content == '':
        print('>>> プログラムを終了します。')
        break

    print('>>> 英文字のみで構成されているか：', end='')

    if repattern.fullmatch(content):
        print('yes\n')
    else:
        print('no\n')
