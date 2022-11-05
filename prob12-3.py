# ===============課題12 11/10===============

import re

# 文字列の先頭が英文字で始まるパターン
pattern = '[a-zA-Z]'
repattern = re.compile(pattern)

while True:
    content = input('>>> ')

    if content == '':
        print('プログラムを終了します。')
        exit()

    print('>>> 英文字で始まるか：', end='')
    check = repattern.match(content)
    if check:
        print('yes\n')
    else:
        print('no\n')
