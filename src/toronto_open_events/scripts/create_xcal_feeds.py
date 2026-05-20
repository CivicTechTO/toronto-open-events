from open_event_feed.exporters import xcal_from_event_items
from open_event_feed.event_item import EventItem
from .data_collection import all_event_feeds
from os import listdir


def run():
    for (event_feed, name) in all_event_feeds():
        destination = "../../scraped_data/feeds/" + name + ".xcal"
        xcal_from_event_items(event_feed, destination)
