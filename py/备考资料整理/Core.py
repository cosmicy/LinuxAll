


def InsertNum(listtxt, num, lineIn):
    for index,item in enumerate(listtxt):
        if item.find(str(num),0,3) == 0:
            #line = lineIn.replace(str(num-1),'答案')
            listtxt.insert(index, '答案略\n' if lineIn == '\n' else '答案'+lineIn)
            break

def ReadTimu(timufile, daanfile):
    #读取题目文件
    timu=[]
    with open(timufile,encoding='utf-8') as timutxt:
        for line in timutxt:
            timu.append(line)
    #读取答案文件
    with open(daanfile,encoding='utf-8') as daantxt:
        for index, item in enumerate(daantxt):
            InsertNum(timu, index+2, item)
    #写入结果文件
    with open("result.txt", 'w',encoding='utf-8') as result:
        result.write(''.join(timu))