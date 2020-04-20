#自动生成指定网段IP地址
print("*****随机生成指定部分ip:******")
iplist=[]
a=10
while a<1 or a>4:
    a=int(input('请输入想要随机生成的IP地址的部分：1.2.3.4: '))
if a == 1:
    sec=input('请输入固定IP地址的第二部分：')
    thir=input('请输入固定IP地址的第三部分：')
    four=input('请输入固定IP地址的第四部分：')
    fir=0
    for i in range(0,255):
        fir += 1
        ip=str(fir)+'.'+sec+'.'+thir+'.'+four+'\n'
        iplist.append(ip)
        print(fir,'.',sec,'.',thir,'.',four,sep='')
elif a == 2:
    fir=input('请输入固定IP地址的第一部分：')
    thir=input('请输入固定IP地址的第三部分：')
    four=input('请输入固定IP地址的第四部分：')
    sec=0
    for j in range(0,255):
        sec += 1
        ip=fir+'.'+str(sec)+'.'+thir+'.'+four+'\n'
        iplist.append(ip)
        print(fir,'.',sec,'.',thir,'.',four,sep='')
elif a == 3:
    fir=input('请输入固定IP地址的第一部分：')
    sec=input('请输入固定IP地址的第二部分：')
    four=input('请输入固定IP地址的第四部分：')
    thir=0
    for j in range(0,255):
        thir += 1
        ip=fir+'.'+sec+'.'+str(thir)+'.'+four+'\n'
        iplist.append(ip)
        print(fir,'.',sec,'.',thir,'.',four,sep='')
elif a == 4:
    fir=input('请输入固定IP地址的第一部分：')
    sec=input('请输入固定IP地址的第二部分：')
    thir=input('请输入固定IP地址的第三部分：')
    four=0
    for j in range(0,255):
        four += 1
        ip=fir+'.'+sec+'.'+thir+'.'+str(four)+'\n'
        iplist.append(ip)
        print(fir,'.',sec,'.',thir,'.',four,sep='')
        
#写入文件       
fp=open('IPlist.txt','w')
fp.writelines(iplist)
fp.close()






