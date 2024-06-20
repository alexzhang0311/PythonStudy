from concurrent.futures import ThreadPoolExecutor,as_completed
import requests,re,time,concurrent
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



def getinfo(url):
    # 发送请求并获取响应
    response = requests.get(url)
    # print(response)
    rsp = response.text
    print(f'{url} {len(rsp)}')
    return rsp

def parserHtml(response):

    soup = BeautifulSoup(response, 'html.parser')
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
    

    # data.to_csv(f"./1.csv",encoding='utf-8',mode='a',header=False,index=False)

    # print('thread %s ended.' % threading.current_thread().name)
    return data


if __name__ == "__main__":
    
    starttime = time.time()
    location_En = 'ns'
    threads = []
    location = location_map.get(location_En)
    allpage = int(getlastpage(location)) + 1 
    print(f"{location} 共有{allpage}页房源信息")
    urls = [ f'https://shenzhen.leyoujia.com/esf/{location}/?n={page}' for page in range(1,allpage)]
    
    #pool-map模式，不能随时提交任务，只能把任务按照列表准备好；按顺序进行返回
    with concurrent.futures.ThreadPoolExecutor() as pool:
        htmls = pool.map(getinfo,urls)
        htmls = list(zip(urls,htmls))


    print("craw ended")

    #pool-submit 模式 单个提交任务
    with concurrent.futures.ThreadPoolExecutor() as pool:
        futures = {}
        for url,html in htmls:
            data = pool.submit(parserHtml,html)
            futures[data] = url

        #按照顺序返回
        for future,url in futures.items():
            print(f'{url}\n{future.result()}')

        #哪个任务先执行完成，则先打印结果
        for future in  concurrent.futures.as_completed(futures):
            url = futures.get(future)
            print(url,future.result())

    

    