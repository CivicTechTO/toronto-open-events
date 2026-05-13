from open_event_feed.exporters import xcal_from_event_items
from open_event_feed.event_item import EventItem
from os import listdir

def create_xcal_feeds(filename):
    set_of_data = []

    with open("./scraped_data/" + filename, "r") as f:
        for line in f:
            ei = EventItem.fromJSON(line)
            set_of_data.append(ei)

    xcal_from_event_items(set_of_data, "./scraped_data/feeds/" + filename[:-6] + ".xcal")

if __name__ == "__main__":
    for f in listdir("./scraped_data"):
        if f[-6:] == ".jsonl":
            create_xcal_feeds(f)