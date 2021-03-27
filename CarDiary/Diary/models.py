from django.db import models

# Create your models here.

class Car(models.Model):

    manufacter = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vin = models.CharField(max_length=50)

    def __str__(self):
        return self.vin

class TO(models.Model):
    date = models.DateTimeField(blank=True)
    whatdone = models.CharField(max_length=500, blank=True)
    workcost = models.IntegerField(max_length=500, blank=True, default=0)
    detailscost = models.IntegerField(max_length=500, blank=True, default=0)
    mileage = models.IntegerField(max_length=500, blank=True)
    vin = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='Team1')




    def __int__(self):
        return self.pk