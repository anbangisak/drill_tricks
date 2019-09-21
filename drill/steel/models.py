import datetime

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

    WEEK = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    date = models.DateField(blank=True)
    open = models.FloatField(default=0.0)
    close = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    turnover = models.FloatField(default=0.0)
    share_traded = models.BigIntegerField(default=0)

    def filter_by_date(self, request):
        """
        Filter recording using date range
        """
        strt_dt = datetime.datetime.strptime(request.POST['start'], '%d/%m/%Y')
        end_dt = datetime.datetime.strptime(request.POST['end'], '%d/%m/%Y')
        units = AdUnits.objects.filter(date__range=[strt_dt, end_dt])
        return units
