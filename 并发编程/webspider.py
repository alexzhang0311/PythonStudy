import requests,re,time,threading
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



def getinfo(lock,location,page):
    # print('thread %s is running...' % threading.current_thread().name)
    # 定义目标URL
    url = f'https://shenzhen.leyoujia.com/esf/{location}/?n={page}'
    print(url)
    
    # 发送请求并获取响应
    response = requests.get(url)
    # print(response.status_code)
    # 如果请求失败则抛出异常
    response.raise_for_status()

    # 使用BeautifulSoup解析HTML页面
    soup = BeautifulSoup(response.text, 'html.parser')

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
            location1 = location_area.split('|')[4]
        except:
            print("数据格式不规范:{}".format(location_area))


        unitprice = re.search(r'\d+', items.select_one('div.price p.sub').text).group()

        raw = items.select_one('div.btn.im-zixun.fl.jjs_bd_log')

        forward = raw.get("data-forward")
        area = raw.get("data-area")
        layout = raw.get("data-attr")
        price = raw.get("data-price")

        locationList.append(location1)
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

    print(data)
    
    lock.acquire()
    try:
        data.to_csv(f"C:/Users/alexxzhang/Desktop/house/{location_En}.csv",encoding='utf-8',mode='a',header=False,index=False)
    finally:
        lock.release()
    # print('thread %s ended.' % threading.current_thread().name)
    return True


if __name__ == "__main__":
    
    starttime = time.time()
    location_En = 'ba'
    threads = []
    location = location_map.get(location_En)
    allpage = int(getlastpage(location)) + 1 
    lock = threading.Lock()
    print(f"{location} 共有{allpage}页房源信息")

    # print('thread %s is running...' % threading.current_thread().name)
    for page in range(1,allpage):
        
        # rsp = getinfo(location,page)
        t = threading.Thread(target=getinfo, args=(lock,location,page,),name='LoopThread')
        threads.append(t)
        
        # if rsp:
        #     print('location:{} page:{} success!'.format(location,page))
        # else:
        #     print('location:{} page:{} false!'.format(location,page))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()
        # print('thread %s ended.' % threading.current_thread().name)
    
    endtime  = time.time()

    print("用时：",endtime-starttime)