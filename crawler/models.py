from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=350)
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_("updated time"), auto_now=True)
    is_enabled = models.BooleanField(verbose_name=_("is_enabled"), default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=130, blank=True)
    price = models.CharField(verbose_name=_("price"), max_length=50, blank=True)
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name=_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')