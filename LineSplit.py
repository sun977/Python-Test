#分割一以多位输出
def long_to_2(str_,num):
  num=int(num)
  for i in range(0,len(str_)+1,num):
      print(str_[i:i+num])
    
data=input("要分割的字符串：")
num=input("分割成几个一组：")
long_to_2(data,num)


