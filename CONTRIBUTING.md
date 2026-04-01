## Getting started

We are always accepting new people writing scrapers for this project! To get started first find an issue, or create one for the site you wish to scrape from the github scraper tag https://github.com/CivicTechTO/toe/issues?q=is%3Aissue%20state%3Aopen%20label%3Ascraper .
After you have an issue you will need to clone the github repository, then install the dependencies with

```sh
uv install
```

Then you will want to create a scraper with the command

```sh
uv run python scripts/new_scraper.py scraper_name
```

It is important to note the name _must_ be in camel case. You can find your newly found scraper in `src/event_scrapers/event_scrapers/spiders/scraper_name_spider.py`

Most of creating a scraper will be finding what selector will get the list of events, and then inside of each event what selectors can find the title, datetime, description, URL, etc inside of each event. To learn more about selectors read more about them here https://docs.scrapy.org/en/latest/topics/selectors.html .

The best way to try these out will be using the Scrapy shell `uv run scrapy shell {URL}` (docs here: https://docs.scrapy.org/en/latest/topics/shell.html) and then edit the individual attributes in the scraper class.

You can then run your scraper with

```
uv run scrapy crawl scraper_name
```

and you can check the data inside of `scr/scraped_data/scraper_name.jsonl`
