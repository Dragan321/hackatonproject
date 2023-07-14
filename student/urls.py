
from .views import loginView, registerView, addCreditCard, successMessage, addBank, studentView, logoutView, applyThird, accountSettings, applyFirst, applySecond

from django.urls import path

urlpatterns = [

    path("", studentView, name='studentView'),
    path("login", loginView, name='login'),
    path("register", registerView, name='register'),
    path("logout", logoutView, name='logout'),
    path("connect-credit-card", addCreditCard, name='addCreditCard'),
    path("connect-bank", addBank, name='addBank'),
    path("account-settings", accountSettings),
    path("apply/first-form", applyFirst),
    path("apply/second-form", applySecond),
    path("apply/third-form", applyThird),
    path("apply/success-message", successMessage),

]