import math,time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

Preme = [112272530952111193] * 4

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))

    for i in range(3,sqrt_n,2):
        if n % i == 0:
            return False
    
    return True


def single_thread():
    for number in Preme:
        is_prime(number)
        print(number)



def multi_thread():
    with ThreadPoolExecutor() as executor:
        results = executor.map(is_prime,Preme)

def multi_process():
    with ProcessPoolExecutor() as executor:
        result = executor.map(is_prime,Preme)


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print(f"单线程耗时：{end-start}")

    start = time.time()
    multi_thread()
    end = time.time()
    print(f"多线程耗时：{end-start}")

    start = time.time()
    multi_process()
    end = time.time()
    print(f"多进程耗时：{end-start}")
