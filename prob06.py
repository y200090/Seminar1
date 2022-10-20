# ===============課題6 10/20===============

sentence = '"これは本文を用いたPythonについての日本語処理のテストです。"'
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
    
    entry = input('  >> ')
    if entry == '':
        # プログラム終了
        exit()
    print('\n', end='')
    temp = entry.split()

    if len(temp) == 3:
        forward = temp[0]
        target = temp[1]
        backward = temp[2]

        if forward in sentence and backward in sentence:
            forward_position = sentence.find(forward)
            backward_position = sentence.find(backward)

            sentence = list(sentence)
            if forward_position + len(forward) == backward_position:
                sentence.insert((forward_position + len(forward)), target)

            else:
                print(f'"{backward}"は"{forward}"の直後にありません。\n')   
        else:
            print('文字列が存在しません。\n')

    elif len(temp) == 2:
        before = temp[0]
        after = temp[1]

        if before in sentence:
            sentence = sentence.replace(before, after)

        else:
            print(f'置換する文字列{before}が存在しません。\n')

    elif len(temp) == 1:
        target = temp[0]

        if target in sentence:
            sentence = sentence.replace(target, '')
        
        else:
            print(f'削除する文字列{target}が存在しません。\n')
                
    sentence = ''.join(sentence)
    print(sentence, end='\n')
