
import datetime
import scrapy
from open_event_feed.event_item import EventItem
from abstract_scraper import AbstractScraper


class TheGarrisonSpider(AbstractScraper):
    name = "the_garrison"
    start_urls = ["http://www.garrisontoronto.com/"]

    ORGANIZER_NAME = "The Garrison"
    ORGANIZER_LINK = "http://www.garrisontoronto.com/"

    def get_all_events(self, response):
        return response.css("#calendar_wrap")

    def get_event_title(self, event_html):
        return event_html.css("#calendar_info_headliner ::text").get()

    def get_event_url(self, event_html):
        return event_html.css(".calendar_info_doors_cover a::attr(href)").get()

    # Input like ['SATURDAY', 'MAY', '02']
    def get_start_date(self, event_html):
        parts = event_html.css("#calendar_date ::text").getall()
        parts = [s.strip() for s in parts if s.strip()]
        _, month_str, day_str = parts[:3]

        # BabyG has specific styling of making 0's to o's 'o2' -> '02'
        day_str = day_str.replace('o', '0').replace('O', '0')

        today = datetime.datetime.now()
        year = today.year

        # Try with current year first
        date_str = f"{month_str} {day_str} {year}"
        parsed_date = datetime.datetime.strptime(date_str, "%B %d %Y")
        
        # If it's in the past, roll forward to next year
        if parsed_date.date() < today.date():
            parsed_date = parsed_date.replace(year=year + 1)
        
        return parsed_date

