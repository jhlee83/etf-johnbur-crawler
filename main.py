import crawler.crawler as crawler
import json
import time
import datetime
from google.cloud import firestore


def main():
    with open('./crawler/etfs-data.json', 'r') as f:
        etf_data_dic = json.load(f)
    etf_crawled_array = []
    for data in etf_data_dic["etfs"]:
        result_dict = {"ticker": data["ticker"]}
        result_dict["result"] = crawler.crawler(
            data["asset_manager"], data["url"])
        etf_crawled_array.append(result_dict)
        time.sleep(3)
    etf_crawled_result = {
        "crawled_date": firestore.SERVER_TIMESTAMP}
    # "crawled_date": datetime.date.today().strftime('%Y-%m-%d')}
    etf_crawled_result["crawled_array"] = etf_crawled_array
    print(etf_crawled_result)
    # db = firestore.Client()
    # doc_ref = db.collection(u'etfs-info')
    # doc_ref.add(etf_crawled_result)


if __name__ == "__main__":
    main()
