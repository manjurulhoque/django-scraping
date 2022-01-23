from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes_scraper import settings as my_settings
from scrapy.settings import Settings

from quotes_scraper.spiders.quotes import QuotesSpider


class Command(BaseCommand):
    help = "Release the scraper"

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        # process = CrawlerProcess(get_project_settings())
        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(QuotesSpider)
        process.start()
