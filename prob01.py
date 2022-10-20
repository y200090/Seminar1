# ===============課題1 09/29===============

# s1 = "123"
# s2 = "456789"

# s1 = input('s1 = ')
# s2 = input('s2 = ')

# r1 = s1 + s2               # 文字列を連結
# r2 = int(s1) + int(s2)     # 文字列を数値変換して計算

# print(f'r1 = {r1}')
# print(f'r2 = {r2}')

# ===================発展===================

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

def devel():
    s1 = ""
    s2 = ""

    while True:
        s1 = input('s1 = ')
        if s1 == "quit":
            print('\n  >> "quit"が入力されました。プログラムを終了します。')
            return
        if s1 == "":
            print('\n  >> "Enterキー"が押されました。プログラムを終了します。')
            return

        # 整数の判定
        if is_int(s1) == False:
            # 少数の判定
            if is_float(s1) == False:
                print(' >> s1に数字以外の文字列が入力されました。数字を入力してください。')
                continue
            else:
                s1 = float(s1)
        else:
            s1 = int(s1)

        s2 = input('s2 = ')
        if s2 == "quit":
            print('\n >> "quit"が入力されました。プログラムを終了します。')
            return
        if s2 == "":
            print('\n >> "Enterキー"が押されました。プログラムを終了します。')
            return

        # 整数の判定
        if is_int(s2) == False:
            # 少数の判定
            if is_float(s2) == False:
                print(' >> s2に数字以外の文字列が入力されました。数字を入力してください。')
                continue
            else:
                s2 = float(s2)
        else:
            s2 = int(s2)

        r1 = str(s1) + str(s2)    # 文字列の結合
        r2 = s1 + s2              # 数値計算

        print(f'r1 = {r1}')
        print(f'r2 = {r2}\n')

devel()
