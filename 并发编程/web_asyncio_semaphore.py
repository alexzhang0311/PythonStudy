import asyncio
import aiohttp
import time,re
from bs4 import BeautifulSoup
import pandas as pd


urlList = [
    f'https://shenzhen.leyoujia.com/esf/a3/?n={page}' for page in range(1,51)
]


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
    print(data)
    

    # data.to_csv(f"./1.csv",encoding='utf-8',mode='a',header=False,index=False)

    # print('thread %s ended.' % threading.current_thread().name)
    # return data


#控制并发度
semaphore = asyncio.Semaphore(10)

# print(urlList)

htmlList = []
async def async_craw(url):
    async with semaphore:
        print("craw url:",url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as rsep:
                result = await rsep.text()
                parserHtml(result)
                # htmlList.append(result)
                # await asyncio.sleep(1)
                print(f'craw url:{url},{len(result)}')

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url)) for url in urlList
]


start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
# for html in htmlList:
#     parserHtml(html)
end = time.time()

print(end-start)