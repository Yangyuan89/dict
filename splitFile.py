
#读取文件名列表
file = open('D:\\1测试\\标题.txt','r',encoding='utf-8')
line = file.readline()
title_list = []
while line:
    if line.isspace():
        line = file.readline()

    else:
        line = line.strip() +'.txt'
        title_list.append(line)
        line = file.readline()

#print(title_list)
#读取待分割文件

file = open('D:\\1测试\\9000句口语.txt','r',encoding='utf-8')
line = file.readline()


fileContentList = []
a = 0
while line:

    if line.isspace():
        line = file.readline()
    else:

        if('LinNingTTS20220704211734' not in line):
            fileContentList.append(line)
        else:
            path = 'D:\\1测试\\9000句口语\\' + title_list[a].replace('\ufeff','')
            fileArticle = open(path,'a', encoding='utf-8')
            for content in fileContentList:
                fileArticle.write(content)
            fileContentList = []
            fileArticle.close()
            a = a + 1

        line = file.readline()
