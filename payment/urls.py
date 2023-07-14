from .views import getPaymentHistory
from django.urls import path

urlpatterns = [

    path("history", getPaymentHistory, name='getPaymentHistory'),
    

]