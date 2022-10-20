# ===============課題2 10/06===============

# a = [100, 10]
# b = ['滋賀', '大津']
# c = "龍谷大学"

# a.extend(b)
# a.append(c)

# print(a)

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

a = []
while True:
    s = input('  >> リストに追加する文字列を入力してください。：')
    if s == "quit":
        print('  >> "quit"が入力されました。リストへの追加を終了します。\n')
        break
    if s == "":
        print('  >> "Enterキー"が押されました。リストへの追加を終了します。\n')
        break

    if is_int(s) == True:
        s = int(s)
    elif is_float(s) == True:
        s = float(s)

    a.append(s)
    print(f'現在のリストの中身: {a}\n')

del a[:2]
print(f'  >> 先頭2つの要素を削除しました。\n現在のリストの中身: {a}\n')

a.pop(-2)
print(f'  >> 後ろから2番目の要素を削除しました。\n現在のリストの中身: {a}\n')

a[0] = '京都'
print(f'  >> 先頭の要素を "京都" に置き換えました。\n現在のリストの中身: {a}\n')

b = ['滋賀', '大津']

a.append(b)
print(f'  >> リストの中にリストを追加しました。\n現在のリストの中身: {a}\n')

print(f'リストの中身を出力します。リストの要素数: {len(a)}\n')
# for i in range(len(a)):
#     if type(a[i]) is list:
#         print(f'\n  >> リストの中にリストがありました。\nリストの中身を出力します。リストの要素数: {len(a[i])}\n')
#         for j in range(len(a[i])):
#             print(f'{a[i][j]}')
#     else:
#         print(f'{a[i]}')
for x in a:
    if type(x) is list:
        # print(f'\n  >> リストの中にリストがありました。\nリストの中身を出力します。リストの要素数: {len(x)}\n')

        for y in x:
            print(y)
    else:
        print(x)
