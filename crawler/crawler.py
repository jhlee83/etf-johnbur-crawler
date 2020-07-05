import requests
from bs4 import BeautifulSoup
import json
import sys
import traceback
from re import sub
import datetime
import logging

logging.basicConfig(level=logging.ERROR)


def crawler(asset_manager, url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            if asset_manager == "Blackrock":
                aum_pre = soup.find(
                    "div", class_="col-totalNetAssets").find("span", class_="data").string.strip()
                aum = float(sub(r'[^\d.]', '', aum_pre))
                aum_date_pre = soup.find("div", class_="col-totalNetAssets").find(
                    "span", class_="as-of-date").string.strip('\n').strip('as of')
                aum_date = datetime.datetime.strptime(
                    aum_date_pre, "%b %d, %Y").strftime('%Y-%m-%d')
                ytm = float(soup.find("div", class_="col-yieldToWorst").find("span",
                                                                             class_="data").string.strip().strip('%'))
                ytm_date_pre = soup.find("div", class_="col-yieldToWorst").find(
                    "span", class_="as-of-date").string.strip('\n').strip('as of')
                ytm_date = datetime.datetime.strptime(
                    ytm_date_pre, "%b %d, %Y").strftime('%Y-%m-%d')
                prem = float(soup.find("div", class_="col-premiumDiscountPercent").find(
                    "span", class_="data").string.strip().strip('%'))
                prem_date_pre = soup.find("div", class_="col-premiumDiscountPercent").find(
                    "span", class_="as-of-date").string.strip('\n').strip('as of')
                prem_date = datetime.datetime.strptime(
                    prem_date_pre, "%b %d, %Y").strftime('%Y-%m-%d')
                dur = float(soup.find("div", class_="col-modelOad").find("span",
                                                                         class_="data").string.strip().strip('yrs'))
                dur_date_pre = soup.find("div", class_="col-modelOad").find(
                    "span", class_="as-of-date").string.strip('\n').strip('as of')
                dur_date = datetime.datetime.strptime(
                    dur_date_pre, "%b %d, %Y").strftime('%Y-%m-%d')
                wam = float(soup.find("div", class_="col-weightedAvgLife").find(
                    "span", class_="data").string.strip().strip('yrs'))
                wam_date_pre = soup.find("div", class_="col-weightedAvgLife").find(
                    "span", class_="as-of-date").string.strip('\n').strip('as of')
                wam_date = datetime.datetime.strptime(
                    wam_date_pre, "%b %d, %Y").strftime('%Y-%m-%d')
                expr = float(soup.find(
                    "tr", class_="fee-code-expr").find("td", class_="data").string.strip('%'))
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
                result["expr"] = expr
                print(json.dumps(result))
                return json.dumps(result)
            elif asset_manager == "Invesco":
                ytm = float(soup.find_all("div", class_="widget gray-bg stacked")
                            [3].find_all("span", class_="pull-right")[0].string.strip().strip('%'))
                ytm_wam_date_pre = soup.find_all("div", class_="widget gray-bg stacked")[
                    3].find_all("span", class_="asofdatetime")[0].string.strip().strip('as of')
                ytm_wam_date = datetime.datetime.strptime(
                    ytm_wam_date_pre, "%m/%d/%Y").strftime('%Y-%m-%d')
                wam = float(soup.find_all("div", class_="widget gray-bg stacked")
                            [3].find_all("span", class_="pull-right")[1].string.strip())
                expr = float(soup.find_all("div", class_="widget gray-bg stacked")
                             [4].find_all("span", class_="pull-right")[10].string.strip().strip('%'))
                expr_date_pre = soup.find_all("div", class_="widget gray-bg stacked")[
                    4].find_all("span", class_="asofdate")[0].string.strip().strip('as of')
                expr_date = datetime.datetime.strptime(
                    expr_date_pre, "%m/%d/%Y").strftime('%Y-%m-%d')
                aum_pre = soup.find_all("div", class_="widget gray-bg stacked")[5].find_all(
                    "span", class_="pull-right")[9].string.strip().strip('M')
                aum = 1000000*float(sub(r'[^\d.]', '', aum_pre))
                aum_date_pre = soup.find_all("div", class_="widget gray-bg stacked")[5].find_all(
                    "span", class_="asofdatetime")[0].string.strip().strip('as of')
                aum_date = datetime.datetime.strptime(
                    aum_date_pre, "%m/%d/%Y").strftime('%Y-%m-%d')
                result = {}
                result["aum"] = aum
                result["aum_date"] = aum_date
                result["ytm"] = ytm
                result["ytm_date"] = ytm_wam_date
                result["wam"] = wam
                result["wam_date"] = ytm_wam_date
                result["expr"] = expr
                result["expr_date"] = expr_date
                return json.dumps(result)
            else:
                print("Asset manager is not available")
                pass
        else:
            print("html page does not exist", "\nErrorcode : ", r.status_code)
            pass
    except Exception as e:
        print("Error occured", e)
        traceback.print_exc()
        pass


if __name__ == "__main__":
    crawler(*sys.argv[1:])
