import flask,time,json
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor(max_workers=3)

def file1():
    time.sleep(0.1)
    data=pd.read_csv("C:/Users/alexxzhang/Desktop/house/1.csv",index_col=0)
    return data.to_json(orient='records',force_ascii=False)

def file2():
    time.sleep(0.2)
    data=pd.read_csv("C:/Users/alexxzhang/Desktop/house/2.csv",index_col=0)
    return data.to_json(orient='records',force_ascii=False)

def file3():
    time.sleep(0.3)
    data=pd.read_csv("C:/Users/alexxzhang/Desktop/house/3.csv",index_col=0)
    return data.to_json(orient='records',force_ascii=False)

@app.route("/")
def index():
    ###多线程时间取决于时间最长的函数
    data1 = pool.submit(file1)
    data2 = pool.submit(file2)
    data3 = pool.submit(file3)

    return json.dumps({
        "data1":data1.result(),
        "data2":data2.result(),
        "data3":data3.result()
    },ensure_ascii=False)
    #单线程时间为各个函数时间相加
    # data1 = file1()
    # data2 = file2()
    # data3 = file3()

    # return json.dumps({
    #     "data1":data1,
    #     "data2":data2,
    #     "data3":data3
    # },ensure_ascii=False)
    

if __name__ == "__main__":
    app.run(port=8080)