from os import listdir
from open_event_feed.event_item import EventItem

BASE_URL = "../../scraped_data/"


def events_from_feed(name):
    set_of_data = []

    with open(BASE_URL + name, "r") as f:
        for line in f:
            try:
                ei = EventItem.fromJSON(line)
                set_of_data.append(ei)
            except:
                TypeError
                pass

    return set_of_data


def all_event_feeds():
    for f in listdir(BASE_URL):
        if f[-6:] == ".jsonl":
            yield (events_from_feed(f), f[:-6])
