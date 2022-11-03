# ===============課題10 11/3===============

# from collections import Counter

words = ['机', '本', '机', '机', '本', '学校', '大学']

dict_words = {}

for x in words:
    dict_words[x] = words.count(x)

print(f'{dict_words}\n')

# # キーに要素、値に出現回数を持つCounterオブジェクト(dictのサブクラス)を作成
# dict_words = Counter(words)
# # 出現回数順に並べ替えたリストを辞書に変換
# print(dict(dict_words.most_common()), '\n')

for key, value in dict_words.items():
    print(f'{key}: {value}回')
