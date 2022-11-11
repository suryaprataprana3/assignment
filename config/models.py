from django.db import models

class CryptoTable(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    one_hour_per = models.FloatField(null=True, blank=True, default=0)
    twenty_four_hour_per = models.FloatField(null=True, blank=True, default=0)
    seven_day_per = models.FloatField(null=True, blank=True, default=0)
    market_cap = models.FloatField(null=True, blank=True, default=0)
    volume = models.FloatField(null=True, blank=True, default=0)
    supply = models.FloatField(null=True, blank=True, default=0)
