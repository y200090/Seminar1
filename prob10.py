# ===============課題10 11/3===============

from collections import Counter

words = ['机', '本', '机', '机', '本', '学校', '大学']

# 重複した要素を持たないリストを作成
unduplicated_words = list(set(words))

appearance = []
for word in unduplicated_words:
    # 要素の出現回数を取得
    apcount = words.count(word)
    appearance.append(apcount)

# 2つのリストを辞書に変換
dict_words = dict(zip(unduplicated_words, appearance))
print(dict_words)
print('\n', end='')

# # キーに要素、値に出現回数を持つCounterオブジェクト(dictのサブクラス)を作成
# dict_words = Counter(words)
# # 出現回数順に並べ替えたリストを辞書に変換
# print(dict(dict_words.most_common()), '\n')

for key, value in dict_words.items():
    print(f'{key}: {value}回')
