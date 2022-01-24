from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes_scraper import settings as my_settings
from scrapy.settings import Settings
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import signals

from quotes_scraper.spiders.quotes import QuotesSpider


class ReactorControl:
    def __init__(self):
        self.crawlers_running = 0

    def add_crawler(self):
        self.crawlers_running += 1

    def remove_crawler(self):
        self.crawlers_running -= 1
        if self.crawlers_running == 0:
            reactor.stop()


def setup_crawler():
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    # process = CrawlerProcess(get_project_settings())
    process = CrawlerProcess(settings=crawler_settings)

    process.crawl(QuotesSpider)
    process.start()


reactor_control = ReactorControl()


class Command(BaseCommand):
    help = "Release the scraper"

    def handle(self, *args, **options):
        # setup_crawler()
        # reactor.run()

        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        # process = CrawlerProcess(get_project_settings())
        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(QuotesSpider)
        process.start()
