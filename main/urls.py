from .views import getHome, aboutPage, sendPayment, confirmPayment, paymentSuccess
from django.urls import path

urlpatterns = [

    path("", getHome, name='home'),
    path("about-us", aboutPage),
    path("send-payment", sendPayment),
    path("confirm-payment", confirmPayment),    
    path("payment-successful", paymentSuccess),


]