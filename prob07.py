# ===============課題7 10/27===============

# import re
# from _module.convert_half import conv_half

# # 全角文字列を判定する関数
# # 全角文字列であればTrueを返す
# def isFullWidth(vaule):
#     return re.match(r'^[^\x01-\x7E]+$', value) is not None

dic = {}
with open('data/07.dat', 'r', encoding='utf-8') as f:
    for line in f:
        key, value = line.split()
        dic[key] = value

print('\n    --ディクショナリ--')
print(f'    {dic}\n')

while True:

    entry = input('>>> 検索: 1, 追加: 2, 削除: 3, 終了: q(or Enter only) を入力してください: ')
    
    # if isFullWidth(entry) == True:
    #     entry = conv_half(entry)

    if entry == 'q' or entry == 'ｑ' or entry == '':
    # if entry == 'q' or entry == '':
        print('>>> プログラムを終了します。')
        break

    else:
        # 検索処理
        if entry == '1' or entry == '１':
        # if entry == '1':

            while True:
                s_key = input('>>> 検索キーを入力(end with Enter): ')

                if s_key == '':
                    break
                
                if s_key in dic:
                    print('\n>>> \033[42m このキーは存在します。 \033[0m \n>>> 対応している値は以下です。\n')
                    print(f'    {dic[s_key]}')
                    break
                
                else:
                    print('\n>>> \033[41m このキーは存在しません。 \033[0m')
                    print('>>> 存在しているキーは以下です。以下のキーに対する処理を行ってください。\n')

                    for key in dic.keys():
                        print(f'    {key}')
                    print('\n', end='')
                    continue
            print('\n', end='')
            continue

        # 追加処理
        elif entry == '2' or entry == '２':
        # elif entry == '2':

            while True:
                add = input('>>> データを追加(end with Enter): ')

                if add == '':
                    break

                if not len(add) == 2:
                    print('\n>>> \033[41m キーと値はセットで入力してください。 \033[0m')
                    print('\n', end='')
                    continue
                
                else:
                    add_key, add_value = add.split()
                    dic[add_key] = add_value
                    print('\n    --追加後のデータ--')
                    print(f'    {dic}\n')
                    break
            continue
        
        # 削除処理
        elif entry == '3' or entry == '３':
        # elif entry == '3':

            while True:
                del_key = input('>>> 削除キーを入力(end with Enter): ')

                if del_key == '':
                    break
                
                post_dic = dic.pop(del_key, None)
                if post_dic == None:
                    print('\n>>> \033[41m このキーは存在しません。 \033[0m')
                    print('>>> 存在しているキーは以下です。以下のキーに対する処理を行ってください。\n')

                    for key in dic.keys():
                        print(f'    {key}')
                    print('\n', end='')
                    continue

                else:
                    print('\n    --削除後のデータ--')
                    print(f'    {dic}\n')
                    break
            continue

        else:
            print('>>> 適切な値を入力し直してください。\n')
            continue
