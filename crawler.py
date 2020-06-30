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
            if asset_manager == "Blackrock":
                with open('./crawl-info.json', 'r') as f:
                    crawl_info_dic = json.load(f)
                selector = crawl_info_dic["Blackrock"]["selectors"]
                aum = soup.select(selector["aum"])[0].find("span",class_="data").string.strip()
                aum_date = soup.select(selector["aum"])[0].find("span",class_="as-of-date").string
                ytm = soup.select(selector["ytm"])[0].find("span",class_="data").string.strip()
                ytm_date = soup.select(selector["ytm"])[0].find("span",class_="as-of-date").string
                prem = soup.select(selector["prem"])[0].find("span",class_="data").string.strip()
                prem_date = soup.select(selector["prem"])[0].find("span",class_="as-of-date").string
                dur = soup.select(selector["dur"])[0].find("span",class_="data").string.strip()
                dur_date = soup.select(selector["dur"])[0].find("span",class_="as-of-date").string
                wam = soup.select(selector["wam"])[0].find("span",class_="data").string.strip()
                wam_date = soup.select(selector["wam"])[0].find("span",class_="as-of-date").string
                expr = soup.find("tr",class_="fee-code-expr").find("td",class_="data").string
                result = {}
                result["aum"] = aum
                result["aum_date"] = aum_date
                result["ytm"] = ytm
                result["ytm_date"] = ytm_date
                result["prem"] = prem
                result["prem_date"] = prem_date
                result["dur"] = dur
                result["dur_date"] = dur_date
                result["wam"] = wam
                result["wam_date"] = wam_date
                print(result)                                 
                return result
            elif asset_manager == "Invesco":                
                ytm = soup.find_all("div",class_="widget gray-bg stacked")[3].find_all("span",class_="pull-right")[0].string.strip()
                ytm_wam_date = soup.find_all("div",class_="widget gray-bg stacked")[3].find_all("span",class_="asofdatetime")[0].string.strip()
                wam = soup.find_all("div",class_="widget gray-bg stacked")[3].find_all("span",class_="pull-right")[1].string.strip()
                expr = soup.find_all("div",class_="widget gray-bg stacked")[4].find_all("span",class_="pull-right")[10].string.strip()
                expr_date = soup.find_all("div",class_="widget gray-bg stacked")[4].find_all("span",class_="asofdate")[0].string.strip()
                aum = soup.find_all("div",class_="widget gray-bg stacked")[5].find_all("span",class_="pull-right")[9].string.strip()
                aum_date = soup.find_all("div",class_="widget gray-bg stacked")[5].find_all("span",class_="asofdatetime")[0].string.strip()
                print(ytm,wam,ytm_wam_date,expr,expr_date,aum,aum_date)
            else:
                print("Asset manager is not available")
                pass
        else: 
            print("html page does not exist","\nErrorcode : ",r.status_code)
            pass
    except:
        print("Error occured")
        pass

if __name__ == "__main__":
    crawler(*sys.argv[1:])