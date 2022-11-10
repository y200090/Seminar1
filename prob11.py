# ===============課題11 11/10===============

# ファイルからデータをリストに読み込む関数
def rd(fname, x):
    with open(f'data/{fname}', 'r', encoding='utf-8') as f:
        for line in f:
            x.append(line.rstrip())

    return len(x)

filename = ['11-1.dat', '11-2.dat']
a = []
b = []
c = []

for fname, x in zip(filename, [a, b]):
    num = rd(fname, x)
    print(f'ファイル"{fname}"から・・・\n{num}: {x}\n')

c.extend([len(a), len(b), a, b])
print(f'併合リスト:\n{c}\n')

print('併合リストの各要素:\n' + ' '.join(list(map(str, c))))
# for d in c:
#     print(f'{d}', end=' ')
# print('\n', end='')
