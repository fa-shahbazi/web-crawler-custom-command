from django.core.management.base import BaseCommand

from crawler._assets import crawler
from crawler._assets.urls import links
from crawler.models import Product, Category
from crawler._assets.urls import mapper


class Command(BaseCommand):
    help = "prints hello world"

    def handle(self, *args, **options):
        for url in links:
            data = crawler.crawl_product(url, 2)
            category = data.pop(0)
            category = mapper[category]
            category = Category.objects.create(title=category)
            for product in data:
                Product.objects.create(category=category, **product)