from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    CATEGORIES = (
        ("","mobile_phone"),
        ("","cable"),
        ("","cover"),
        ("","headphones"),
        ("","screen_protector"),
        ("","computer_eqipment"),
        ("","audiovisiual"),
        ("","powerbank"),
        ("","smartwatch"),
        ("","game console"),
        ("","xiaomi accessories")
    )
    url = models.CharField(verbose_name=_("url"), max_length=350, Choices=CATEGORIES)


class Product(models.Model):
    product_name = models.CharField(verbose_name=_("name"), max_length=130)
    product_price = models.CharField(verbose_name=_("price"), max_length=50)
    product_category = models.ForeignKey(Category, verbose_name=_('product_category'), on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name=_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now= True)

    def __str__(self):
        return self.product_name








