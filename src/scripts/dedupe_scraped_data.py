from open_event_feed.event_item import EventItem
from sets import Set

def dedupe_scraped_data(filepath):
    set_of_data = Set()

    with open(filepath, "r") as f:
        for line in f:
            ei = EventItem.fromJSON(line)
            set_of_data.add(ei)

    with open(filepath, "w") as f:
        for ei in set_of_data:
