from open_event_feed.event_item import EventItem
import scrapy

class AbstractScraper(scrapy.Spider):
    name = ""
    start_urls = []

    additional_data_for_all = {}

    def parse(self, response):
        event_htmls = self.get_all_events(response)
        for e in event_htmls:
            yield self.event_html_to_object(e)

    def get_start_date(self, event_html):
        """
        @param event_html: html object of a single event
        @return: datetime object of start date
        """
        raise NotImplementedError

    def get_event_title(self, event_html):
        """
        @param event_html: html object of a single event
        @return: string of event name/title
        """
        raise NotImplementedError

    def get_event_organizer(self, event_html):
        """
        @param event_html: html object of a single event
        @return: string of the name of event organizer/venue
        """
        raise NotImplementedError

    def get_event_url(self, event_html):
        """
        @param event_html: html object of a single event
        @return: string of the event url. Unique per event
        """
        raise NotImplementedError

    def get_event_description(self, event_html):
        """
        @param event_html: html object of a single event
        @return: string of the event description
        """
        return None

    def get_event_location(self, event_html):
        """
        @param event_html: html object of a single event
        @return: string of the event location
        """
        return None

    def get_event_addition_data(self, event_html):
        """
        @param event_html: html object of a single event
        @return: string of the event location
        """
        return {}

    def get_all_events(self, response):
        """
        @param reponse: scrapy response object
        @return: array of html selectors
        """
        raise NotImplementedError

    def event_html_to_object(self, event_html):
        event_attributes = {
            "title": self.get_event_title(event_html),
            "link": self.get_event_url(event_html),
            "organizer_link": self.ORGANIZER_LINK,
            "organizer_name": self.ORGANIZER_NAME,
            "start_datetime": self.get_start_date(event_html),
            "description": self.get_event_description(event_html),
            "location": self.get_event_location(event_html),
            "additional_data": {**self.get_event_addition_data(event_html), **self.additional_data_for_all}
        }
        event_attributes = {k: v for k, v in event_attributes.items() if v is not None or v is not {} or v is not []}

        return EventItem(**event_attributes)

