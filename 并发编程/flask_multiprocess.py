import math,time,flask,json
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


app = flask.Flask("__name__")

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

@app.route("/is/prime/<numbers>")
def prime(numbers):

    # rsp = {}
    number_list = [int(x) for x in numbers.split(",")]

    results = processpool.map(is_prime,number_list)
    return json.dumps(dict(zip(number_list,results)))

    # mapList = list(zip(number_list,results))

    # for data in mapList:
    #     number = data[0]
    #     judge = data[1]
    #     rsp[number] = judge

    # return rsp



if __name__ == "__main__":
    processpool = ProcessPoolExecutor()
    app.run()