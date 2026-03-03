from django.db import models
from django.utils import timezone

#Expense Tracker


class ExpenseTracker(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class Received(models.Model):
  expensetracker = models.ForeignKey(ExpenseTracker , on_delete=models.CASCADE , related_name="receiced")
  sr_no = models.CharField(max_length=100)
  date = models.DateTimeField(default=timezone.now)
  received_from = models.CharField(max_length=100)
  description = models.CharField(max_length=1000 , default="Description")
  amount = models.DecimalField(max_digits=10 , decimal_places=1)

  
class ReceivedImages(models.Model):
  received = models.ForeignKey(Received , on_delete=models.CASCADE , related_name="received_images")
  image = models.ImageField(upload_to='received_image/')


class Spend(models.Model):
  expensetracker = models.ForeignKey(ExpenseTracker , on_delete=models.CASCADE , related_name="spend")
  sr_no = models.CharField(max_length=100)
  date = models.DateTimeField(default=timezone.now)
  sent_to = models.CharField(max_length=100)
  description = models.CharField(max_length=1000 , default="Description")
  amount = models.DecimalField(max_digits=10 , decimal_places=1)


class SpendImages(models.Model):
  spend = models.ForeignKey(Spend , on_delete=models.CASCADE , related_name="spend_images")
  image = models.ImageField(upload_to='spend_image/')  






