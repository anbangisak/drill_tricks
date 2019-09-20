from django.db import models

# Create your models here.

class BaseStamp(models.Model):
    """
    Every CRUD operation timestamps mapping in all requesting model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AdUnits(BaseStamp):
    """
    AdUnits Intel for Distribution and Analytics
    """
    date = models.DateField(blank=True)
    open = models.FloatField(default=0.0)
    close = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    turnover = models.FloatField(default=0.0)
    share_traded = models.BigIntegerField(default=0)
