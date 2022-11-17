# ===============課題8 10/27===============

sentence = '''
龍谷大学先端理工学部{0}課程
{1}さん
こんにちは！'''

with open('assets/08a.dat', 'r', encoding='utf-8') as f:
    for line in f:
        dic = {}
        key, value = line.split()
        print(sentence.format('\033[31m' + key + '\033[0m', '\033[31m' + value + '\033[0m'))

# datas = []
# for data in datas:
#     sentence = '''
#     龍谷大学先端理工学部X課程
#     Yさん
#     こんにちは！'''
#     for key in data.keys():
#         sentence = sentence.replace('X', '\033[31m' + key + '\033[0m')
        
    
#     for value in data.values():
#         sentence = sentence.replace('Y', '\033[31m' + value + '\033[0m')
    
#     print(sentence, end='')
# print('\n')

# for data in datas:
#     sentence = '''
#     龍谷大学先端理工学部{X}課程
#     {Y}さん
#     こんにちは！'''
    
#     for key in data.keys():
#         sentence = sentence.format(X='\033[31m' + key + '\033[0m', Y='\033[31m' + data[key] + '\033[0m')

#     print(sentence, end='')
# print('\n')

