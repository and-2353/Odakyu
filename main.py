import urllib.parse
import requests
from bs4 import BeautifulSoup

def getObject():
    with open('stations.txt', 'r', encoding='utf-8') as f:
        stations = f.readlines()
        stations = [item.rstrip('\n') for item in stations]
    return stations
"""
def makeURL(g_station, day, hour, s_station='生田(神奈川県)'):
    url = 'https://www.odakyu.jp/change/transfer_result/?targetstart=&roughEstimate=co2&startName='
    encoded_s_station = urllib.parse.quote(s_station)
    url += encoded_s_station
    url += '&start=&start=&orvCode=0.0.00004682.%E7%94%9F%E7%94%B0%28%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C%29&orvAdd=&startPosType=&orvPosType=1&goalName='
    encoded_g_station = urllib.parse.quote(g_station)
    url += encoded_g_station
    url += '&goal=&goal=&dnvCode=0.0.00004254.%E6%96%B0%E5%AE%BF&dnvAdd=&goalPosType=&dnvPosType=1&day='
    url += day
    url += '&hour='
    url += hour
    url += '&minute=00&year=&month=&basis=1&useRomancecar=false&sort=0&wspeed=standard&method=0&type='
    return url
"""
def makeURL(g_station, day, hour, s_station='生田(神奈川県)'):
    url = 'https://www.navitime.co.jp/transfer/searchlist?'
    url += 'orvStationName='
    url += urllib.parse.quote(s_station)
    url += '&orvStationCode=00004682'
    url += '&dnvStationName='
    url += urllib.parse.quote(g_station)
    url += '&dnvStationCode=00004254&'
    url += 'month=2022/03'
    url += '&day=24'
    url += '&hour=09'
    url += '&minute=00&basis=1&airplane=1&sprexprs=1&utrexprs=1&othexprs=1&mtrplbus=1&intercitybus=1&ferry=1&sort=2&isrec=1&from=view.transfer.searchlist.tab.change'
    return url


def searchTime(stations):
    url = makeURL('下北沢', '20220324', '09')
    with open('url.txt', mode='w', encoding='utf-8') as f:
        f.write(url)
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    #print(soup)
    elems = soup.find_all(class_="layout-mainArea")
    print(elems)

    with open('time.txt', mode='w', encoding='utf-8') as f:
        for elem in elems:
            f.write(elem.text+'\n')


if __name__ == '__main__':
    stations = getObject()
    searchTime(stations)
    hours = ['09', '11', '13', '15', '17', '19'] 