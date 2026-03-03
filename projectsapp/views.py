from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import ExpenseTracker , Received , Spend
from .serializers import ExpenseTrackerSerializers , ReceivedSerializers , SpendSerializers
from rest_framework.permissions import IsAuthenticated


class ExpenseTrackerAPIVeiw(ListCreateAPIView):
  queryset = ExpenseTracker.objects.all()
  serializer_class = ExpenseTrackerSerializers
  permission_classes = [IsAuthenticated]

class ExpenseTrackerIDAPIView(RetrieveUpdateDestroyAPIView):
  queryset = ExpenseTracker.objects.all()
  serializer_class = ExpenseTrackerSerializers  
  permission_classes = [IsAuthenticated]


class ReceivedAPIView(ListCreateAPIView):
  queryset = Received.objects.all()
  serializer_class = ReceivedSerializers
  permission_classes = [IsAuthenticated]


class ReceivedIDAPIView(RetrieveUpdateDestroyAPIView):
  queryset = Received.objects.all()
  serializer_class = ReceivedSerializers
  permission_classes = [IsAuthenticated]



class SpendAPIView(ListCreateAPIView):
  queryset = Spend.objects.all()
  serializer_class = SpendSerializers
  permission_classes = [IsAuthenticated]


class SpendIDAPIView(RetrieveUpdateDestroyAPIView):
  queryset = Spend.objects.all()
  serializer_class = SpendSerializers
  permission_classes = [IsAuthenticated]