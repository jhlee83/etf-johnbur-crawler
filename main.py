from crawler import crawler
import json
import time
# import time

#
#if soup.h1.string == "Pardon Our Interruption...":
#    print("They detected we are a bot. We hit a captcha.")
#else:
#    price = soup.select("#fundamentalsAndRisk > div.product-data-list.data-points-en_US > div.float-left.in-right.col-yieldToWorst")[0]
#    ytm = price.find("span",class_="data").string
#    print(ytm)

# r = requests.get("https://www.invesco.com/us/financial-products/etfs/product-detail?ticker=BKLN")
# html = r.text

# soup = BeautifulSoup(html, "html.parser")
# time.sleep(1)
# if soup.h1.string == "Pardon Our Interruption...":
#     print("They detected we are a bot. We hit a captcha.")
# else:
# #    price = soup.select_all("div.widget.gray-bg.stacked.canadian")
#     price = soup.find_all("div",class_="widget gray-bg stacked")[3].find_all("span",class_="pull-right")[0].string
# #    ytm = price.find("span",class_="data").string
#     return price

def main() :
    with open('./etfs-data.json', 'r') as f:
        etf_data_dic = json.load(f)
    etf_result_data = []
    for data in etf_data_dic["etfs"]:
        result_dict = {"ticker": data["ticker"]}
        result_dict["ytm"] = crawler(data["asset_manager"],data["url"])
        etf_result_data.append(result_dict)
        print(etf_result_data)
        time.sleep(3)

if __name__ == "__main__":
    main()