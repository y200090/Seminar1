# ===============課題11 発展===============

# ファイルからデータをリストに読み込む関数
def rd(fname, x):
    with open(f'data/{fname}', 'r', encoding='utf-8') as f:
        for line in f:
            x.append(line.rstrip())
            
    return len(x)

# 二つのリストを併合してリストに格納する関数
def proc(x, y):
    c = []
    c.extend([len(x), len(y), x, y])
    return c

filename = ['11-1.dat', '11-2.dat']
a = []
b = []

for fname, x in zip(filename, [a, b]):
    num = rd(fname, x)
    print(f'ファイル"{fname}"から・・・\n{num}: {x}\n')

d = proc(a, b)
print(f'併合リスト:\n{d}\n')

print('併合リストの各要素:\n' + ' '.join(list(map(str, d))))
# for d in d:
#     print(f'{d}', end=' ')
# print('\n', end='')
