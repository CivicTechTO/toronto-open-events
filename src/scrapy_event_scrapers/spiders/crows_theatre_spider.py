from urllib.parse import urlencode
import scrapy
import datetime
from abstract_scraper import AbstractScraper
from urllib.parse import urljoin

class CrowsTheatreSpider(AbstractScraper):
    name = "crows_theatre"
    start_urls = ["https://www.crowstheatre.com/shows-events/schedule?p=10"]

    ORGANIZER_NAME = "Crows Theatre"
    ORGANIZER_LINK = "https://www.crowstheatre.com/"

    # def parse(self, response):
    #     available_months = response.xpath('//select[@id="select-month"]/option')
    #     for available_month in available_months:
    #         val = available_month.attrib["value"]
    #         next_url = self.start_urls[0] + urlencode({"month": val})
    #         yield response.follow(next_url, self.parse_event_page)

    def get_all_events(self, response):
        return response.xpath('//div[@class="schedule"]/div')

    def get_event_title(self, event_html):
        return event_html.css(".title ::text").get()

    def get_event_url(self, event_html):
        return urljoin(
            self.ORGANIZER_LINK,
            event_html.css(".title a::attr(href)").get()
        )

    def get_event_organizer(self, event_html):
        # Static in this case
        return self.ORGANIZER_NAME

    def get_location(self, event_html):
        return event_html.css(".details ::text").getall()[3]

    def get_start_date(self, event_html):
        """
        Example input: " Saturday 2  May   1:30pm"
        """
        date_string = "".join(event_html.css(".date ::text").getall())
        date_string = date_string.replace("\t", "")
        date_string = date_string.replace("\n", " ")
        time_string = event_html.css(".details ::text").getall()[5]
        datetime_string = date_string + " " + time_string

        now = datetime.datetime.now()

        cleaned = " ".join(datetime_string.split())

        parts = cleaned.split(" ", 1)[1]

        temp_dt = datetime.datetime.strptime(parts, "%d %B %I:%M%p")
        temp_dt = temp_dt.replace(year=now.year)

        # If already passed, move to next year
        if temp_dt < now:
            temp_dt = temp_dt.replace(year=now.year + 1)
        
        return temp_dt