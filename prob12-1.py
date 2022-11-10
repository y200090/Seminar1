# ===============課題12 11/10===============

import re

contents = ['abcdefg', 'cdabefg']

pattern = 'ab'
repattern = re.compile(pattern)

for content in contents:
    print(f'文字列: {content} パターン: {pattern}\n')

    mcheck = bool(repattern.match(content))
    print(f'Match chceck  : {mcheck}')

    scheck = bool(repattern.search(content))
    print(f'Search chceck : {scheck}\n')

    # if repattern.match(content):
    #     print('Match chceck  : True')
    # else:
    #     print('Match chceck  : False')

    # if repattern.search(content):
    #     print('Search chceck : True\n')
    # else:
    #     print('Search chceck : False\n')
