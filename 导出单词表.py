import jsonlines
#with open("test.json", "r",encoding='UTF-8') as read_content:
 #   print(json.load(read_content))
#fp = open('新东方商务英语.json', 'w', encoding='utf-8')
#json_data=[]
# i=1
# fp = open('temp.json', 'w', encoding='utf-8')
# for line in open('新东方商务英语BEC_2.json', 'r', encoding='utf-8'):
#     if(i==1):
#         if(str(line).strip() != '"bookId": "CET4luan_1"'):
#             fp.write(str(line).strip())
#
#         else:
#             fp.write(str(line).strip())
#             fp.write('}')
#             fp.write('\n')
#             i=0
#     else:
#         i=1
# fp.close()
#
# with open('temp.json', 'r',encoding='utf-8') as f:
#     word_file = open("商务英语词汇.txt",'w',encoding='UTF-8')
#     for item in jsonlines.Reader(f):
#         print(item['headWord'])
#         word_file.write(item['headWord'])
#         word_file.write('\n')


with open('F:\dict\单词列表\人教版初中\PEPChuZhong9_1.json', 'r',encoding='utf-8') as f:
    word_file = open("F:\dict\单词列表\人教版初中\人教版初中英语-九年级全册551个.txt", 'w', encoding='UTF-8')
    for item in jsonlines.Reader(f):
        #print(item)
        #输出单词
        #print(item['headWord'])
        word_file.write(item['headWord'])
        word_file.write('\n')
    word_file.close()