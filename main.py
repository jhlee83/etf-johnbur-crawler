from crawler import crawler
import json
import time

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