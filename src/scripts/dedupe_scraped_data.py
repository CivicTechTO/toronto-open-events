from open_event_feed.event_item import EventItem
from os import listdir

def dedupe_scraped_data(filepath):
    set_of_data = set()

    with open(filepath, "r") as f:
        for line in f:
            print(line)
            ei = EventItem.fromJSON(line)
            set_of_data.add(ei.toJSON())
    
    with open(filepath, "w") as f:
        f.write("")

    with open(filepath, "a") as f:
        for ei in set_of_data:
            f.write(ei + "\n")

if __name__ == "__main__":
    for f in listdir("./scraped_data"):
        if f[-6:] == ".jsonl":
            dedupe_scraped_data("./scraped_data/" + f)