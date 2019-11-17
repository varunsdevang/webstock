from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .models import User, Portfolio, Stock, Bonds, MutualFunds, HedgeFunds, Cash
from django.template import RequestContext
from django.utils import timezone


# Create your views here.

def home(request):
    if 'username' in request.COOKIES:
        print(request.COOKIES)
        return render(request, 'base.html')
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        # print(request.POST['username'], request.POST['password'])
        for i in User.objects.all():
            if request.POST['username'] == i.user_Name:
                print(i.user_Name,i.user_Password)
                if request.POST['password'] == i.user_Password:
                    response = render(request, 'base.html')
                    response.set_cookie('last_connection', timezone.now())
                    response.set_cookie('username', i.user_Name)
                    return response
    return redirect('/')
