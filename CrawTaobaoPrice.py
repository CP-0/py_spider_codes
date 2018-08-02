import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"price\"\:\"[\d.]*\"', html)
        tlt = re.findall(r'\"title\"\:\".*?\"', html)
        tilt = re.findall(r'\"tag_info\"\:.*?]{1}', html)
        for i in range(len(plt)):
            price = "￥" + eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            tglt = re.findall(r'\"tag\"\:\"(.*?)\"', tilt[i])
            feature = ', '.join(tglt)
            ilt.append([price, title, feature])
    except:
        print('')


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称", "特色"))
    count = 0
    for j in ilt:
        count = count + 1
        print(tplt.format(count, j[0], j[1], j[2]))


def main():
    goods = "手机"
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(i * 48)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
