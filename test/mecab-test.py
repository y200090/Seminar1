import MeCab

# tokenizer = MeCab.Tagger('-r /dev/null -d /var/lib/mecab/dic/mecab-ipadic-neologd')
tokenizer = MeCab.Tagger()

sentence = "鬼滅の刃もいいけれど、約束のネバーランドもいいね"

print(tokenizer.parse(sentence))
