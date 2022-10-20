# ===============課題5 10/20===============

with open('05.dat', 'r', encoding='utf-8') as f:
    str = f.read().split()

text = input('置換前部分文字列と置換後文字列を入力: ')
temp = text.split()

before = temp[0]
after = temp[1]

for x in str:
    if before in x:
        x = x.replace(before, after)
    print(x)
