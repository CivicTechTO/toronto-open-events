from open_event_feed.event_item import EventItem
from os import listdir
from .data_collection import all_event_feeds


def dedupe_scraped_data(filepath):
    set_of_data = set()

    with open(filepath, "r") as f:
        for line in f:
            print(line)
            ei = EventItem.fromJSON(line)
            set_of_data.add(ei.toJSON())


def run():
    for (event_feed, name) in all_event_feeds():
        set_of_data = set(map(lambda x: x.toJSON(), event_feed))
        set_of_data = list(set_of_data)

        filepath = "../../scraped_data/" + name + ".jsonl"

        with open(filepath, "w") as f:
            f.write("")

        with open(filepath, "a") as f:
            for ei in set_of_data:
                f.write(ei + "\n")
