# ===============課題8 10/27===============

data = []
with open('08a.dat', 'r', encoding='utf-8') as f:
    for line in f:
        dic = {}
        n_key, n_value = line.split()
        dic[n_key] = n_value
        data.append(dic)

# for str in data:
#     sentence = '''
#     龍谷大学先端理工学部X課程
#     Yさん
#     こんにちは！'''
#     for key in str.keys():
#         sentence = sentence.replace('X', '\033[31m' + key + '\033[0m')
        
    
#     for value in str.values():
#         sentence = sentence.replace('Y', '\033[31m' + value + '\033[0m')
    
#     print(sentence, end='')
# print('\n')

for str in data:
    sentence = '''
    龍谷大学先端理工学部{X}課程
    {Y}さん
    こんにちは！'''
    
    for key in str.keys():
        sentence = sentence.format(X='\033[31m' + key + '\033[0m', Y='\033[31m' + str[key] + '\033[0m')

    print(sentence, end='')
print('\n')

