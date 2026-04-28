# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class EventScrapersPipeline:
    def process_item(self, item, spider):
        with open(self.scraper_file_name(spider), "a+") as file:
            file.write(item.toJSON() + "\n")

        return item

    def scraper_file_name(self, spider):
        return "../scraped_data/" + spider.name + ".jsonl"
