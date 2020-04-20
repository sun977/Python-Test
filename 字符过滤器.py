print("****字符过滤器****")
infile=input("需要过滤的文件：")
keys=input("输入过滤关键字：")
outfile=input("保存到：")

fp=open(infile,'r',encoding='utf-8')
#fp=open(infile,'r')
#文件编码格式错误请修改默认文件编码
data=fp.readlines()
fp.close()

f=open(outfile,'w',encoding='utf-8')
for i in data:
  lines = filter(lambda ch: ch not in keys, i) #过滤
  ndata=list(lines)
  print(ndata)
  f.writelines(ndata)
f.close()
print("已完成对关键字的过滤")
