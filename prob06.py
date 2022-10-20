# ===============課題6 10/20===============

sentence = '"これは本文を用いたPythonについての日本語処理のテストです。"'
print('\n', end='')
print(sentence, end='\n')

while True:    
    announce = '''
    上文に対し、
    挿入なら"前の文字列　挿入文字列　後ろの文字列"を
    置き換えなら"旧文字列 新文字列"を
    削除なら"削除する文字列"を
    Enterキーのみで終了
    '''
    print(announce, end='\n')
    
    entry = input('>>> ')
    if entry == '':
        # プログラム終了
        print('>>> Enterキーが押されました。プログラムを終了します。')
        exit()
    
    print('\n', end='')
    order = entry.split()

    if len(order) == 3:
        front = order[0]    # 前の文字列
        target = order[1]   # 挿入文字列
        rear = order[2]     # 後ろの文字列

        # 文字列のインデックスを検索(存在しなければ-1を返す)
        f_position = sentence.find(front)
        r_position = sentence.find(rear)

        # 文字列の存在を確認
        if not f_position == -1 and not r_position == -1:
            # 前の文字列の長さを取得
            f_length = len(front)

            # 文字列を挿入するインデックスを取得
            t_index = f_position + f_length

            if t_index == r_position:
                # 文字列を挿入
                sentence = sentence[:t_index] + '\033[31m' + target + '\033[0m' + sentence[t_index:]

                # リスト化
                # sentence = list(sentence)
                # sentence.insert(t_index, '\033[31m' + target + '\033[0m')

            else:
                print(f'>>> \033[41m 文中に文字列"{rear}"は文字列"{front}"の直後ではない！！ \033[0m \n')   
        else:
            print(f'>>> "{front}"または"{rear}"が文中に存在しません。\n')

    elif len(order) == 2:
        before = order[0]   # 旧文字列
        after = order[1]    # 新文字列

        # 文字列の存在を確認
        if before in sentence:
            # 文字列を置換
            sentence = sentence.replace(before, '\033[31m' + after + '\033[0m')

        else:
            print(f'>>> \033[41m 置換する文字列"{before}"が存在しません。 \033[0m \n')

    elif len(order) == 1:
        target = order[0]   # 削除する文字列

        # 文字列の存在を確認
        if target in sentence:
            # 文字列を削除
            sentence = sentence.replace(target, '')
        
        else:
            print(f'>>> \033[41m 削除する文字列"{target}"が存在しません。 \033[0m \n')
                
    # リストの要素を連結
    # sentence = ''.join(sentence)
    
    print(sentence, end='\n')
