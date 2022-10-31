# ===============課題9 11/3===============

words = ['机', '本', '机', '机', '本', '学校', '大学']

# 重複した要素を削除したset型のオブジェクトを作成
unduplicated_words = set(words)
print(unduplicated_words)
print('\n', end='')

unduplicated_words = list(unduplicated_words)

# dict_words = dict.fromkeys(words)
# unduplicated_words = list(dict_words)

# unduplicated_words = sorted(set(words), key=words.index)

for i, word in enumerate(unduplicated_words, 1):
    if i == len(unduplicated_words):
        print(f'{word}')
    else:
        print(f'{word}', end=',')
