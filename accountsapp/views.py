from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import Business , Ledgers , MaineDiye , MaineLiye
from .serializers import BusinessSerializers , LedgerSerializers , MaineDiyeSerializers , MaineLiyeSerializers
from rest_framework.permissions import IsAuthenticated



class CreateListAPIView(ListCreateAPIView):
  queryset = Business.objects.all()
  serializer_class = BusinessSerializers
  permission_classes = [IsAuthenticated]


class RetriveDeleteUpdateAPIView(RetrieveUpdateDestroyAPIView):
  queryset = Business.objects.all()
  serializer_class = BusinessSerializers
  permission_classes = [IsAuthenticated]




class CreateLedgerAPIView(ListCreateAPIView):
  queryset = Ledgers.objects.all()
  serializer_class = LedgerSerializers
  permission_classes = [IsAuthenticated]


class RDULedgerAPIview(RetrieveUpdateDestroyAPIView):
  queryset = Ledgers.objects.all()
  serializer_class = LedgerSerializers  
  permission_classes = [IsAuthenticated]



  
class MaineDiyeAPIView(ListCreateAPIView):
  queryset = MaineDiye.objects.all()
  serializer_class = MaineDiyeSerializers
  permission_classes = [IsAuthenticated]


class MaineDiyeRDUAPIView(RetrieveUpdateDestroyAPIView):
  queryset = MaineDiye.objects.all()
  serializer_class = MaineDiyeSerializers  
  permission_classes = [IsAuthenticated]

  
class MaineLiyeAPIView(ListCreateAPIView):
  queryset = MaineLiye.objects.all()
  serializer_class = MaineLiyeSerializers
  permission_classes = [IsAuthenticated]


class MaineLiyeRDUAPIView(RetrieveUpdateDestroyAPIView):
  queryset = MaineLiye.objects.all()
  serializer_class = MaineLiyeSerializers  
  permission_classes = [IsAuthenticated]