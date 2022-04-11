import jsonlines






word = []
with open('1.json', 'r',encoding='utf-8') as f:
    for item in jsonlines.Reader(f):
        print(item)
        #输出单词
        print(item['word'])

        #输出音标
        if(len(item['phonetic_list'])==4):
         print(item['phonetic_list'][0]+item['phonetic_list'][1]+'  '+item['phonetic_list'][2]+item['phonetic_list'][3])
        elif (len(item['phonetic_list']) == 2):
            print(item['phonetic_list'][0] + item['phonetic_list'][1] )
        else:
            print('')
        #输出单词简单翻译
        print(''.join(item['word_trans_simple']))

        #输出单词朗读文本
        print(''.join(item['word_trans_read']))


        # 输出例句英文
        if(len(item['liju_list'][1])):
            print(item['liju_list'][1][0])
            #输出例句中文
            print(item['liju_list'][0][0])






# with open("cet4.txt",'w',encoding='UTF-8') as f:
#     for i in word:
#         f.write(i)
#         f.write('\n')
#     f.close