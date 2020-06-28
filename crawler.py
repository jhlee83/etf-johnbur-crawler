import requests
from bs4 import BeautifulSoup
import sys
import json 

def crawler(asset_manager, url):
    try :
        r = requests.get(url)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            with open('./crawl-info.json', 'r') as f:
                crawl_info_dic = json.load(f)
            if asset_manager == "Blackrock":
                selector = crawl_info_dic["Blackrock"]["selectors"]                
                aum = soup.select(selector["aum"])[0].find("span",class_="data").string.strip()
                aum_date = soup.select(selector["aum"])[0].find("span",class_="as-of-date").string
                ytm = soup.select(selector["ytm"])[0].find("span",class_="data").string.strip()
                ytm_date = soup.select(selector["ytm"])[0].find("span",class_="as-of-date").string

                print(aum, aum_date, ytm, ytm_date)
                # return aum
            # elif asset_manager == "Invesco":
            #     ytm = soup.find_all("div",class_="widget gray-bg stacked")[3].find_all("span",class_="pull-right")[0].string.strip()
            #     return ytm
        else: 
            print("html page does not exist","\nErrorcode : ",r.status_code)
            pass
    except Error as e:
        print(e)
        pass

if __name__ == "__main__":
    crawler(*sys.argv[1:])