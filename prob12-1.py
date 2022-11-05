# ===============課題12 11/10===============

import re

contents = ['abcdefg', 'cdabefg']

pattern = 'ab'
repattern = re.compile(pattern)

for content in contents:
    print(f'文字列: {content} パターン: {pattern}\n')
    check_match = repattern.match(content)
    if check_match:
        print('Match chceck  : True')
    else:
        print('Match chceck  : False')

    check_search = repattern.search(content)
    if check_search:
        print('Search chceck : True')
    else:
        print('Search chceck : False')
    
    print('\n', end='')
