#参数：两个TXT文件路径
def ReBlankEnter(infile, outfile):
    infopen = open(infile, 'r',encoding="utf-8")
    outfopen = open(outfile, 'w',encoding="utf-8")
   
    lines = infopen.readlines()#read data
    for line in lines:
        if line.split():
            lines=filter(lambda ch: ch not in ' ',line)#去空格
            outfopen.writelines(lines)
        else:
            outfopen.writelines("")
 
    infopen.close()
    outfopen.close()
   
if __name__=='__main__':
    try:
        print("*****TXT文件去空格空行脚本*******")
        print("输入格式：路径+文件名 ")
        intxt=input("旧文件路径:")
        outtxt=input("新文件路径:")
        ReBlankEnter(intxt, outtxt)
    except Exception as err:
        print(err)
    else:
        print("文件修改成功！")

