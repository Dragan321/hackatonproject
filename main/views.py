from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def getHome(request):
    return render(request, 'home.html', {'user':request.user})


def aboutPage(request):
    return render(request, 'about.html')


def sendPayment(request):
    return render(request, 'send-payment-view.html')

def confirmPayment(request):
    return render(request, 'confirm-payment-view.html')

def paymentSuccess(request):
    return render(request, 'payment-success-view.html')
