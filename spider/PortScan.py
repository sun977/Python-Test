import queue
import socket
import threading
queue = queue.Queue()

class process(threading.Thread):
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.queue = queue
        self.open_port = []
    def run(self):
        while True:
            num = self.queue.get()
            self.numJ(num)
            self.queue.task_done()

    def numJ(self, num):
        sk = socket.socket()
        try:
            sk.connect(("127.0.0.1", num))#这里输入要扫描的主机ip
            print(num , "open")
            self.open_port.append(num)
        except:
            #print(num , "close")
            pass
def main():
    for i in range(5):
        t = process(queue)
        t.setDaemon(True)
        t.start()
    ports = [21,22,23,25,53,69,80,110,135,137,
             161,443,3306,3389,8080,2121,3218,1521,1524,1364,1433,8081,9090]
    for num in ports:
        queue.put(num)
    queue.join()

if __name__ == '__main__':
    main()
