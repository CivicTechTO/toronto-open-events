import event_scrapers.scrapy
import sys
import json
from event_scrapers.scrapy.crawler import CrawlerProcess
from event_scrapers.scrapy.utils.project import get_project_settings
from event_scrapers.scrapy.utils.log import configure_logging


def check_results(spider_name):
    name = "./scraped_data/" + spider_name + ".jsonl"
    print(name)
    with open(name) as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        print(json_str)
        result = json.loads(json_str)
        print(result)

def test_spider(spider_name):
    # get spider
    # run spider
    settings = get_project_settings()
    configure_logging()
    process = CrawlerProcess(settings)
    process.crawl(spider_name)
    process.start()
    # check results
    check_results(spider_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please input your spider name")
        exit(1)

    test_spider(sys.argv[1])

