from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def getPaymentHistory(request):

    return render(request, 'payment-history.html')

