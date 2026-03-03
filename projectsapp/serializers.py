from rest_framework import serializers
from .models import ExpenseTracker , Received , ReceivedImages , Spend , SpendImages
from django.db.models import Sum


class ExpenseTrackerSerializers(serializers.ModelSerializer):
  total_received = serializers.SerializerMethodField()
  total_spend = serializers.SerializerMethodField()
  balance = serializers.SerializerMethodField()
  class Meta:
    model = ExpenseTracker
    fields = ['id' , 'name' , 'total_received' , 'total_spend' , 'balance']

  def get_total_received(self, obj):
        total = obj.receiced.aggregate(total=Sum('amount'))['total']
        return total or 0

  def get_total_spend(self, obj):
        total = obj.spend.aggregate(total=Sum('amount'))['total']
        return total or 0

  def get_balance(self, obj):
        received = self.get_total_received(obj)
        spend = self.get_total_spend(obj)
        return received - spend


class ReceivedImagesSerializers(serializers.ModelSerializer):
  class Meta:
    model = ReceivedImages
    fields = ['id' , 'received' , 'image']    


class ReceivedSerializers(serializers.ModelSerializer):
  images = ReceivedImagesSerializers(many = True , read_only= True)
  upload_images = serializers.ListField(
    child=serializers.ImageField(),
    write_only = True,
    required = False
  )
  class Meta:
    model = Received
    fields = ['id' , 'expensetracker' , 'sr_no' , 'date' , 'received_from' , 'description' , 'amount' , 'images' , 'upload_images']

  def create(self, validated_data):
    images = validated_data.pop('upload_images', [])
    bill = Received.objects.create(**validated_data)

    for img in images:
      ReceivedImages.objects.create(received=bill , image=img)
    
    return bill
  

class SpendImagesSerializers(serializers.ModelSerializer):
  class Meta:
    model = SpendImages
    fields = ['id' , 'received' , 'image']    


class SpendSerializers(serializers.ModelSerializer):
  images = SpendImagesSerializers(many = True , read_only= True)
  upload_images = serializers.ListField(
    child=serializers.ImageField(),
    write_only = True,
    required = False
  )
  class Meta:
    model = Spend
    fields = ['id' , 'expensetracker' , 'sr_no' , 'date' , 'sent_to' , 'description' , 'amount' , 'images' , 'upload_images']

  def create(self, validated_data):
    images = validated_data.pop('upload_images', [])
    bill = Spend.objects.create(**validated_data)

    for img in images:
      SpendImages.objects.create(spend=bill , image=img)
    
    return bill

