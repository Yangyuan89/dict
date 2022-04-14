import jsonlines






word = []
with open('商务英语词汇.json', 'r',encoding='utf-8') as f:
    word_file = open("商务英语词汇导出.txt", 'w', encoding='UTF-8')
    for item in jsonlines.Reader(f):
        #print(item)
        #输出单词
        print(item['word'])
        word_file.write(item['word'])
        word_file.write('\t')
        #输出音标
        if(len(item['phonetic_list'])==4):
         #print(item['phonetic_list'][0]+item['phonetic_list'][1]+'  '+item['phonetic_list'][2]+item['phonetic_list'][3])
         #word_file.write(item['phonetic_list'][0]+item['phonetic_list'][1]+'  '+item['phonetic_list'][2]+item['phonetic_list'][3])
         word_file.write(item['phonetic_list'][3])
         word_file.write('\t')
        elif (len(item['phonetic_list']) == 2):
            #print(item['phonetic_list'][0] + item['phonetic_list'][1])
            word_file.write(item['phonetic_list'][1])
            word_file.write('\t')
        else:
            print('')
            word_file.write('\t')
            word_file.write('\t')
        #输出单词简单翻译
        print(''.join(item['word_trans_simple']))
        word_file.write(''.join(item['word_trans_simple']))
        word_file.write('\t')
        #输出单词朗读文本
        print(''.join(item['word_trans_read']))
        word_file.write(''.join(item['word_trans_read']))
        word_file.write('\t')

        # 输出例句英文
        if(len(item['liju_list'][1])):
            print(item['liju_list'][1][0])
            word_file.write(item['liju_list'][1][0])
            word_file.write('\t')
            #输出例句中文
            print(item['liju_list'][0][0])
            word_file.write(item['liju_list'][0][0])
            word_file.write('\t')

        # 输出短语英文
        if (len(item['wordGroup_list'][1])):
            print(item['wordGroup_list'][0][0])
            word_file.write(item['wordGroup_list'][0][0])
            word_file.write('\t')
            # 输出例句中文
            print(item['wordGroup_list'][1][0])
            word_file.write(item['wordGroup_list'][1][0])
            word_file.write('\t')
        word_file.write('\n')
    word_file.close()
    f.close()



# with open("cet4.txt",'w',encoding='UTF-8') as f:
#     for i in word:
#         f.write(i)
#         f.write('\n')
#     f.close