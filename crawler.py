import requests
from bs4 import BeautifulSoup

def crawler(asset_manager, url):
    try :
        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
    except Error as e:
        print(e)
    if asset_manager == "Blackrock":
        ytm = soup.select("#fundamentalsAndRisk > div.product-data-list.data-points-en_US > div.float-left.in-right.col-yieldToWorst")[0].find("span",class_="data").string.strip()
        return ytm
    elif asset_manager == "Invesco":
        ytm = soup.find_all("div",class_="widget gray-bg stacked")[3].find_all("span",class_="pull-right")[0].string.strip()
        return ytm