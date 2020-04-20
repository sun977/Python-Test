'''
随机生成指定数量IP(支持大数量ip)
'''
import time

time_start = time.time()

def get_ip(number='10', start='1.1.1.1'):
    num=number
    file = open('ip_list.txt', 'w')
    starts = start.split('.')
    A = int(starts[0])
    B = int(starts[1])
    C = int(starts[2])
    D = int(starts[3])
    for A in range(A, 256):
        for B in range(B, 256):
            for C in range(C, 256):
                for D in range(D, 256):
                    ip = "%d.%d.%d.%d" % (A, B, C, D)

                    if number > 1:
                        file.write(ip + '\n')
                        number -= 1
                    elif number == 1:  # 解决最后多一行回车问题
                        file.write(ip)
                        number -= 1
                    else:
                        file.close()
                        print("已生成{}条IP!".format(num))
                        return
                D = 0
            C = 0
        B = 0
print("******随机生成指定数量IP地址*****")
num=eval(input("生成IP的数量："))
start=input("开始的IP:")
print("正在生成....")
get_ip(num, start)
time_end = time.time()
time = time_end - time_start
print('耗时%s秒' % time)
