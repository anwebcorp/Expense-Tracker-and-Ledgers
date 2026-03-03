from django.db import models
from django.utils import timezone

class Business(models.Model):
  bus_name = models.CharField(max_length=100)

  def __str__(self):
    return self.bus_name


class Ledgers(models.Model):  
  business = models.ForeignKey(Business , on_delete=models.CASCADE , related_name="ledgers")
  cutomer_name = models.CharField(max_length=100)

  def __str__(self):
    return self.cutomer_name
  

class MaineDiye(models.Model):
  ledger = models.ForeignKey(Ledgers , on_delete=models.CASCADE , related_name="mainediye")
  sr_no = models.CharField(max_length=100)
  date = models.DateTimeField(default=timezone.now)
  description = models.CharField(max_length=500)
  maine_diye = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.ledger} - {self.sr_no}"


class ManineDiyeImages(models.Model):
  images = models.ForeignKey(MaineDiye , on_delete=models.CASCADE , related_name="images_diye")
  image = models.ImageField(upload_to='maine_diye/')

  def __str__(self):
    return f"image of {self.images.ledger}"
  
  

class MaineLiye(models.Model):
  ledger = models.ForeignKey(Ledgers , on_delete=models.CASCADE , related_name="maineliye")
  sr_no = models.CharField(max_length=100)
  date = models.DateTimeField(default=timezone.now)
  description = models.CharField(max_length=500)
  maine_liye = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.ledger} - {self.sr_no}"


class ManineLiyeImages(models.Model):
  images = models.ForeignKey(MaineDiye , on_delete=models.CASCADE , related_name="images_liye")
  image = models.ImageField(upload_to='maine_liye/')

  def __str__(self):
    return f"image of {self.images.ledger}"
  
