# ===============課題4 発展===============

a = []
with open('data/04-adv.dat', 'r') as f:
    # 2次元配列に読み込む
    for s in f:
        a.append(s.split())
    
    # while True:
    #     s = f.readline()
    #     if s == '':
    #         break
    #     a.append(s.split())
    
print(f'リストの全容: {a}\n')

# for i in range(len(a)):
#     print(f'{i + 1}行目: {a[i]}')
for x in a:
    print(x)

print(f'\nリストの全要素: ', end='')
for x in a:
    for y in x:
        print(y, end=' ')

print('\n', end='')
