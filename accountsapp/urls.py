from django.urls import path
from .views import CreateListAPIView , RetriveDeleteUpdateAPIView , CreateLedgerAPIView , RDULedgerAPIview , MaineLiyeAPIView , MaineLiyeRDUAPIView , MaineDiyeAPIView , MaineDiyeRDUAPIView

urlpatterns = [
    #create and list business
    path('business/', CreateListAPIView.as_view() , name="create_list"),
    #retrieve-update and delete business
    path('business/<int:pk>/', RetriveDeleteUpdateAPIView.as_view(), name="retrieve_update_delete"),
    
    #create and Ledger
    path('ledger/', CreateLedgerAPIView.as_view(), name="create_ledger"),
    #retrieve-update and delete ledger
    path('ledger/<int:pk>/', RDULedgerAPIview.as_view(), name="pk_ledger"),

    
    #craete and list "maine Diye api"
    path('credit/', MaineDiyeAPIView.as_view(), name="create_maine_diye"),
    #retrieve_del_update maine diye
    path('credit/<int:pk>', MaineDiyeRDUAPIView.as_view(), name="retrieve_del_update"),
   
    #craete and list "maine Liye api"
    path('debit/', MaineLiyeAPIView.as_view(), name="create_maine_liye"),
    #retrieve_del_update maine Liye
    path('debit/<int:pk>', MaineLiyeRDUAPIView.as_view(), name="retrieve_del_update"),
]