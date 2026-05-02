from urllib.parse import urlencode
import scrapy


class CrowsTheatreSpider(scrapy.Spider):
    name = "crows_theatre"
    start_urls = ["https://www.crowstheatre.com/shows-events/schedule?p=10"]

    shared_attributes = {
        "organizer": "Crows Theatre",
    }

    def parse(self, response):
        available_months = response.xpath('//select[@id="select-month"]/option')
        for available_month in available_months:
            val = available_month.attrib["value"]
            next_url = self.start_urls[0] + urlencode({"month": val})
            yield response.follow(next_url, self.parse_event_page)

    def parse_event_page(self, response):
        event_htmls = self.get_all_events(response)
        for event in event_htmls:
            yield self.event_html_to_object(event)

    def get_all_events(self, response):
        return response.xpath('//div[@class="schedule"]/div')

    def event_html_to_object(self, event_html):
        return {
            "name": event_html.xpath("*/div[1]/div[2]/text()").get().strip(),
            "organizer": "Crows Theatre",
            "start_date": event_html.xpath("*/div[1]/div[1]/text()").get().strip(),
            "url": event_html.xpath("a/@href").get(),
            "description": event_html.xpath("*/div[1]/div[4]/text()").get().strip(),
        }
