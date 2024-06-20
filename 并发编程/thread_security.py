import threading,time

lock = threading.Lock()

class Account(object):
    def __init__(self, balance:int):
        self.balance = balance

def draw(account,amount):
    with lock:
        if account.balance > amount:
            time.sleep(0.1)
            print(threading.current_thread().name,"取钱成功")
            account.balance -= amount
            print(threading.current_thread().name,f"余额:{account.balance}")
        else:
            print(threading.current_thread().name,"取钱失败")

if __name__ == "__main__":
    account = Account(1000)

    t1 = threading.Thread(name='ta',target=draw,args=(account,800))
    t2 = threading.Thread(name='tb',target=draw,args=(account,800))

    t1.start()
    t2.start()