from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CrawlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crawler'
    verbose_name = _('Crawler')
    verbose_name_plural = _('Crawlers')
