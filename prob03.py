# ===============課題3 10/13===============

# def is_int(s):
#     try:
#         int(s)
#     except ValueError:
#         return False
#     else:
#         return True

# def is_float(s):
#     try:
#         float(s)
#     except ValueError:
#         return False
#     else:
#         return True

a = []
sum = 0
with open('03.dat', 'r') as f:
    for s in f:
        # # 整数の値を判定
        # if is_int(s) == True:
        #     n = s
        # # 少数の値を判定
        # elif is_float(s) == True:
        #     s = float(s)
        s = float(s)
        sum += s
        a.append(s)

# ファイルの行数を取得
n = len(a)

# 平均値を計算
avg = sum / float(n)

print(a)
print(f'n: {n}')
print(f'avg: {round(avg, 1)}')   # 小数点第一位に換算
