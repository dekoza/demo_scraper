from django.contrib.postgres.indexes import BrinIndex
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=3, unique=True, db_index=True)
    rss_link = models.URLField()

    class Meta:
        verbose_name = 'curency'
        verbose_name_plural = 'currencies'


class Rate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        indexes = (
            BrinIndex(fields=['date']),
        )
