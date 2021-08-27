from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    product_name = models.Charfield(verbose_name=_("name"), max_length=130)
    product_price = models.Charfield(verbose_name=_("price"))
    product_category = models.ForeignKey(Category, verbose_name=_('product_category'))
    created_time = models.DateTimeField(verbose_name=_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now= True)

    def __str__(self):
        return self.product_name


class Category(models.model):
    url = models.URLfield(verbose_name=_("url"), max_length=350)






