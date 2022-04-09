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
fp = open('temp.txt', 'w', encoding='utf-8')
with open('temp.json', 'r',encoding='utf-8') as f:
    for item in jsonlines.Reader(f):
        a = str(item['content']['word']).split('sentences')
        if (len(a)>1):
            #print(a)
            print(item['headWord'])
            fp.write(item['headWord'])
            fp.write('\t')
            word_trans = str(item['content']['word']).split('tran')
            word_trans = word_trans[1].split(',')[0].replace('"','').replace('\'','').replace(':','').strip()
            print(word_trans)
            fp.write(word_trans)
            fp.write('\t')
            #print(a)
            sen_eng = a[1].split(': \'')[1].split('\',')[0].strip()
            print(sen_eng)
            fp.write(sen_eng)
            fp.write('\t')
            sen_ch = a[1].split(': \'')[2].split('\'}')[0].strip()
            print(sen_ch)
            fp.write(sen_ch)
            fp.write('\t')
            b = str(item['content']['word']).split('ukphone')
            ukphone = b[1].split(',')[0].replace('"','').replace('\'','').replace(':','').strip()
            print(ukphone)
            fp.write(ukphone)
            fp.write('\t')
            c= str(item['content']['word']).split('usphone')
            if (len(c)>1):
                usphone = c[1].split(',')[0].replace('"','').replace('\'','').replace(':','').strip()
                print(usphone)
                fp.write(usphone)
                fp.write('\t')
            else:
                fp.write('\t')
        fp.write('\n')