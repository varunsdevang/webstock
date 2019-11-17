from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Portfolio, Stock, Bonds, MutualFunds, HedgeFunds, Cash


# Create your views here.

def home(request):
    if 'username' in request.COOKIES:
        print(request.COOKIES)
        return render(request, 'base.html')
    else:
        return render(request, 'login.html')



