# ===============課題5 10/20===============

with open('05.dat', 'r', encoding='utf-8') as f:
    # ファイルの中身を一括で読み込み、改行文字で分割してリストに格納
    str = f.read().split()

# 元の文字列
print('-------')
for x in str:
    print(x)
print('-------\n')

entry = input('>>> 置換前部分文字列と置換後文字列を入力: ')
print('\n', end='')
before, after = entry.split()

print('\n*******')

# 置換対象の文字列を表示
for x in str:
    # 文字列の存在を確認
    if before in x:
        x = x.replace(before, '\033[34m' + before + '\033[0m')
    print(x)

print(' ↓')

# 置換後の文字列(結果)を表示
for x in str:
    # 文字列の存在を確認
    if before in x:
        # 文字列を置換
        x = x.replace(before, '\033[31m' + after + '\033[0m')
    print(x)
