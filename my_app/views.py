from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .models import User, Portfolio, Investment
from django.template import RequestContext
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def home(request):
    if 'username' in request.COOKIES:
        print(request.COOKIES)
        try:
            user = User.users.get(user_Name=request.COOKIES['username'])
            if not user:
                return render(request, 'login.html')
            for port in Portfolio.ports.all():
                if port.user_Portfolio == user:
                    port_name = Portfolio.ports.get(user_Portfolio=user)
                    port_id = port.port_Name
            invs = []
            total = 0
            for inv in Investment.investments.all():
                print(inv, inv.investment_parent)
                if inv.investment_parent == port_name:
                    invs.append(inv)
                    total += inv.investment_amount
            context1 = {'invs': invs, 'total': total, 'user': user, 'name': port_id}
            print("--------------------context---------------------------")
            print(context1)
            return render(request, 'loggedin.html', context=context1)
        except ObjectDoesNotExist:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        # print(request.POST['username'], request.POST['password'])
        for i in User.users.all():
            if request.POST['username'] == i.user_Name:
                print(i.user_Name, i.user_Password)
                if request.POST['password'] == i.user_Password:
                    response = render(request, 'loggedin.html', context={'username': i.user_Name})
                    response.set_cookie('last_connection', timezone.now())
                    response.set_cookie('username', i.user_Name)
                    return response
    return home(request)


def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    if request.method=='POST':
        form=request.POST
        print(form)

        for i in User.users.all():
            if form['username']==i.user_Name:
                message="User already Exists"
                return render(request,'register.html',context={'message':message})
        if int(form['age'])<18 or int(form['age'])>99:
            message="invalid Age"
            return render(request,'register.html',context={'message':message})
        print(form)
        user=User.users.create(user_Name=form['username'],user_DOB=form['age'],user_Password=form['password'],user_Email=form['emailid'])
        Portfolio.ports.create(user_Portfolio=user,port_Name=form['portfolioname'])
        return redirect('/')




