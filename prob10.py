# ===============課題10 11/3===============

words = ['机', '本', '机', '机', '本', '学校', '大学']

# 重複した要素を持たないリストを作成
unduplicated_words = list(set(words))

appearance = []
for word in unduplicated_words:
    cnt = words.count(word)
    appearance.append(cnt)

# 2つのリストを辞書に変換
dict_words = dict(zip(unduplicated_words, appearance))
print(dict_words)
print('\n', end='')

for key in dict_words.keys():
    print(f'{key}: {dict_words[key]}回')
