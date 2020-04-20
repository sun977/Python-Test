#数字不能过大
print("****因素数分解*****")
num=eval(input("输入一个数："))
print(num,end=' ')
print('=',end=' ')
i=1
while i<=num+1:
    r=num%i
    if r==0:  ##余数为0，输出i
        print(i,end=' ')
        num = num/i
        i=1
        if num!=1: ##当num=i时，输出*号
            print('*',end=' ')
    i+=1 ##有余数的时候自增，有余数的时候置1在自增
