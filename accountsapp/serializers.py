from rest_framework import serializers
from .models import Business , Ledgers , MaineDiye , ManineDiyeImages , MaineLiye , ManineLiyeImages
from  django.db.models import Sum

class BusinessSerializers(serializers.ModelSerializer):
  total_diye = serializers.SerializerMethodField()
  total_liye = serializers.SerializerMethodField()
  balance = serializers.SerializerMethodField()
  
  class Meta:
    model = Business
    fields = ['id' , 'bus_name' , 'bus_name' , 'total_diye', 'total_liye' , 'balance']

  def get_total_diye(self, obj):
        from .models import MaineDiye

        return MaineDiye.objects.filter(
            ledger__business=obj
        ).aggregate(
            Sum('maine_diye')
        )['maine_diye__sum'] or 0

  def get_total_liye(self, obj):
        from .models import MaineLiye

        return MaineLiye.objects.filter(
            ledger__business=obj
        ).aggregate(
            Sum('maine_liye')
        )['maine_liye__sum'] or 0  
  
  def get_balance(self, obj):
        total_diye = self.get_total_diye(obj)
        total_liye = self.get_total_liye(obj)

        return total_liye - total_diye


class LedgerSerializers(serializers.ModelSerializer):
  total_diye = serializers.SerializerMethodField()
  total_liye = serializers.SerializerMethodField()
  balance = serializers.SerializerMethodField()
  class Meta:
    model = Ledgers
    fields = ['id' , 'business' , 'cutomer_name' , 'total_diye', 'total_liye', 'balance']    

  def get_total_diye(self, obj):
        return obj.mainediye.aggregate(
            Sum('maine_diye')
        )['maine_diye__sum'] or 0

  def get_total_liye(self, obj):
        return obj.maineliye.aggregate(
            Sum('maine_liye')
        )['maine_liye__sum'] or 0
  
  def get_balance(self, obj):
        total_diye = obj.mainediye.aggregate(
            Sum('maine_diye')
        )['maine_diye__sum'] or 0

        total_liye = obj.maineliye.aggregate(
            Sum('maine_liye')
        )['maine_liye__sum'] or 0

        return total_liye - total_diye



class MaineDiyeImagesSerializers(serializers.ModelSerializer):
  class Meta:
    model = ManineDiyeImages
    fields = ['id' , 'images' , 'image']


class MaineDiyeSerializers(serializers.ModelSerializer):
  images = MaineDiyeImagesSerializers(many = True , read_only = True)
  upload_images = serializers.ListField(
    child=serializers.ImageField(),
    write_only = True,
    required=False,
    allow_empty=True
  )
  class Meta:
    model = MaineDiye
    fields = ['id' , 'ledger' , 'sr_no' , 'date' , 'description' , 'maine_diye' , 'images' , 'upload_images']


  def create(self, validated_data):
    images = validated_data.pop('upload_images' , [])
    bill = MaineDiye.objects.create(**validated_data)

    for image in images:
      ManineDiyeImages.objects.create(images=bill , image=image)

    return bill




class MaineLiyeImageSerializers(serializers.ModelSerializer):
  class Meta:
    model = ManineLiyeImages
    fields = ['id' , 'images' , 'image']


class MaineLiyeSerializers(serializers.ModelSerializer):
  images = MaineLiyeImageSerializers(many = True , read_only=True)
  upload_images = serializers.ListField(
    child=serializers.ImageField(),
    write_only = True,
    required=False,
    allow_empty=True
  )
  class Meta:
    model = MaineLiye
    fields = ['id' , 'ledger' , 'sr_no' , 'date' , 'description' , 'maine_liye' , 'images' , 'upload_images']

  def create(self, validated_data):
    images = validated_data.pop('upload_images' , [])
    bill = MaineLiye.objects.create(**validated_data)

    for image in images:
      ManineLiyeImages.objects.create(images=bill , image=image)
    
    return bill