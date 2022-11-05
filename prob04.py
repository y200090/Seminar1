# ===============課題4 10/13===============

a = []
for i in range(20):
    # 0より大きいかつ偶数の数を判定
    if i > 0 and i % 2 == 0:
        n = i * 10 + 33
        a.append(n)

print(f'a = {a}')

# b = []
with open('data/04.dat', 'r') as f:
    # for s in f:
    #     n = int(s)
    #     b.append(n)
    
    b = f.read().split()
    b = list(map(int, b))

print(f'b = {b}\n')

# 2つのリストを結合
c = a + b

# リストの中身を昇順にソート
d = sorted(c)

# リストの要素の合計値
sum = sum(d)

print(d)
print(f'合計値: {sum}')
