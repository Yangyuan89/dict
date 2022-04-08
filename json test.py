import jsonlines
#with open("test.json", "r",encoding='UTF-8') as read_content:
 #   print(json.load(read_content))
fp = open('temp.json', 'w', encoding='utf-8')
#json_data=[]
i=1
fp = open('temp.json', 'w', encoding='utf-8')
for line in open('CET4luan_1.json', 'r', encoding='utf-8'):
    if(i==1):
        if(str(line).strip() != '"bookId": "CET4luan_1"'):
            fp.write(str(line).strip())

        else:
            fp.write(str(line).strip())
            fp.write('}')
            fp.write('\n')
            i=0
    else:
        i=1
fp.close()

with open('temp.json', 'r',encoding='utf-8') as f:
    for item in jsonlines.Reader(f):
        print(item['headWord'])
        print(str(item['content']['word']['content']).split('sCn')[1])