import json
import jsonlines
import random

# word_info = {}
# word_info.update({'word':'test'})
#
# word_info.update({'word_trans':'测试'})
#
# liju = [['test1','test2','test3','test4'],['测试1','测试2','测试3','测试4']]
#
# print(liju)
# word_info.update({'liju':liju})
#
#
#
# fp1 = open('test1.json', 'w', encoding='utf-8')
# e= json.dumps(word_info)
#
# for i in range(10):
#     fp1.write(e)
#     fp1.write('\n')
#
# fp1.close
# print('\n')

with open('word_items.json', 'r',encoding='utf-8') as f:
    for item in jsonlines.Reader(f):
        print(item)

for i in range(100):
    print(random.randint(50,100))