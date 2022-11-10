# ===============課題13 11/17===============

import re

pattern = re.compile('[a-zA-Z_]\w{,7}$')

contents = ['@bc', '1ab', 'a12', 'a1234567', 'a12345678', '_xyz']

for content in contents:
    print(f'{content}は変数名として適切で', end='')

    if pattern.match(content):
        print('ある\n')
    else:
        print('ない\n')
