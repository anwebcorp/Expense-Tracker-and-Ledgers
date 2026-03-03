from django.urls import path
from .views import ExpenseTrackerAPIVeiw , ExpenseTrackerIDAPIView , ReceivedAPIView , ReceivedIDAPIView , SpendAPIView , SpendIDAPIView


urlpatterns = [
    path('expense/tracker/',  ExpenseTrackerAPIVeiw.as_view(), name="expense_tracker"),
    path('expense/tracker/<int:pk>/',  ExpenseTrackerIDAPIView.as_view(), name="expense_tracker"),
    path('received/',  ReceivedAPIView.as_view(), name="received_api"),
    path('received/<int:pk>/',  ReceivedIDAPIView.as_view(), name="received_api_pk"),
    path('spend/',  SpendAPIView.as_view(), name="spend_api"),
    path('spend/<int:pk>/',  SpendIDAPIView.as_view(), name="spend_api_pk"),
]
