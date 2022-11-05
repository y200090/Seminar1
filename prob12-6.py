# ===============課題12 11/10===============

import re

# 文字列が1文字以上4文字以下の英数字とアンダースコアのみで構成されているパターン
pattern = '\w{1,4}'
repattern = re.compile(pattern)

while True:
    content = input('>>> ')

    if content == '':
        print('プログラムを終了します。')
        exit()

    print('>>> 1文字以上4文字以下の英数字とアンダースコアのみで構成されているか：', end='')
    check = repattern.fullmatch(content)
    if check:
        print('yes\n')
    else:
        print('no\n')
