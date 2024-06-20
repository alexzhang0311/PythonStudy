import requests,re,time,threading,queue,random
import pandas as pd
from bs4 import BeautifulSoup


location_map = {
    "ft":"a1",
    "lh":"a2",
    "ns":"a3",
    "yt":"a4",
    "ba":"a5",
    "lg":"a6",
    "lh":"a7",
    "gm":"a8",
    "ps":"a9",
    "dp":"a10",
    "ss":"a11"

}

def getlastpage(location):
    url = f'https://shenzhen.leyoujia.com/esf/{location}/'
    # 发送请求并获取响应
    response = requests.get(url)
    # 如果请求失败则抛出异常
    response.raise_for_status()

    # 使用BeautifulSoup解析HTML页面
    soup = BeautifulSoup(response.text, 'html.parser')
    lastpage = soup.select('div.jjs-new-page.fr a')[-1].get("title")
    return lastpage


# 定义目标URL
def set_url(url_queue:queue.Queue,location:str,page:int):
    url = f'https://shenzhen.leyoujia.com/esf/{location}/?n={page}'
    url_queue.put(url)
    print(threading.current_thread().name,f'craw {page}',f"url_queue_size:{url_queue.qsize()}")


def html_parse(html):

    soup = BeautifulSoup(html.text, 'html.parser')

    itemGroup = soup.select('li.item.clearfix')

    outcome = {}
    locationList = []
    communityList = []
    forwardList = []
    areaList = []
    layoutList = []
    priceList = []
    unitpriceList = []
    for items in itemGroup:
        try:
            info = items.select('p.attr')[2]
            location_area = re.sub(r'[\n]+|\s+','|',info.get_text())
            community = location_area.split('|')[1]
            home_location = location_area.split('|')[4]
        except:
            print("数据格式不规范:{}".format(location_area))


        unitprice = re.search(r'\d+', items.select_one('div.price p.sub').text).group()

        raw = items.select_one('div.btn.im-zixun.fl.jjs_bd_log')

        forward = raw.get("data-forward")
        area = raw.get("data-area")
        layout = raw.get("data-attr")
        price = raw.get("data-price")

        locationList.append(home_location)
        communityList.append(community)
        forwardList.append(forward)
        areaList.append(area)
        layoutList.append(layout)
        priceList.append(price)
        unitpriceList.append(unitprice)

    outcome["location"] = locationList
    outcome["community"] = communityList
    outcome["forward"] = forwardList
    outcome["area"] = areaList
    outcome["layout"] = layoutList
    outcome["price"] = priceList
    outcome["unitprice"] = unitpriceList

    data = pd.DataFrame(outcome)

    return data

#从URL Queue中获取队列信息并进行IO操作，将返回内容存入html Queue
def getinfo(url_queue: queue.Queue,html_queue:queue.Queue):
    while True:
        url= url_queue.get()
        # 发送请求并获取响应
        html = requests.get(url)
        html_queue.put(html)
        print(threading.current_thread().name,f'craw {url}',f"html_queue_size:{html_queue.qsize()}")
        time.sleep(0.7)
        

#html_queue 队列的xiao
def do_parse(html_queue:queue.Queue):
    while True:
        html = html_queue.get()
        result = html_parse(html)
        # print(result)
        # result.to_csv(f"C:/Users/alexxzhang/Desktop/house/{threading.current_thread().name}.csv",encoding='utf-8',mode='a',header=False,index=False)
        result.to_csv(f"C:/Users/alexxzhang/Desktop/house/1.csv",encoding='utf-8',mode='a',header=False,index=False)
        print(threading.current_thread().name,f'parse',f"html_queue_size:{html_queue.qsize()}")
        # time.sleep(1)



if __name__ == "__main__":
    html_queue = queue.Queue()
    url_queue = queue.Queue()
    location = "ba"
    pages = int(getlastpage(location_map.get(location))) + 1 
    
    for page in range(1,pages):
        set_url(url_queue,location_map.get(location),page)

    for idx in range(3):
        t = threading.Thread(target=getinfo,args=(url_queue,html_queue,),name=f"claw{idx}")
        t.start()

    for idx in range(2):
        t = threading.Thread(target=do_parse,args=(html_queue,),name=f"parse{idx}")
        t.start()