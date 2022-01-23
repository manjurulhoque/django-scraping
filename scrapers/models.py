from django.db import models
from scrapy_djangoitem import DjangoItem


# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    tags = models.JSONField()


class QuoteItem(DjangoItem):
    django_model = Quote
