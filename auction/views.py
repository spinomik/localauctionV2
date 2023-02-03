from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from auction.models import Item
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone
from decimal import Decimal

now = timezone.now()

class home(View):
    def get(self, request):
        items = Item.objects.filter(startDate__lte=now, endDate__gte=now).exclude(status='finished')
        data = {
            'title': 'home',
            'navBar': 'home',
            'items': items,
        }
        messages.success(request,'')
        return render(request, 'pages/index.html', data)

class loginView(View):
    def get(self, request):
        return render(request, 'pages/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Zalogowano jako '+username)
            return HttpResponseRedirect('/index/')
        else:
            messages.success(request,'Niepoprawny login lub hasło')
            return render(request, 'pages/login.html')


class logoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Wylogowano z systemu!')
        return render(request, 'pages/login.html')


class bought(View):
    def get(self, request):
        user = request.user
        items = Item.objects.filter(winner=user)
        data = {
            'title': 'bought',
            'navBar': 'bought',
            'items': items,
        }
        return render(request, 'pages/bought.html', data)


class bidItem(View):
    def post(self, request):
        username = request.POST['username']
        item_id = request.POST['itemId']
        amount = request.POST['amount']
        item = Item.objects.get(pk=item_id)
        if (item.maxPrice > Decimal(amount)):
            messages.success(request, 'Podana kwota jest mniejsza niż aktualna')
            return HttpResponseRedirect('/index/')
        if (item.endDate < now):
            messages.success(request, 'Aukcja już się zakończyła')
            return HttpResponseRedirect('/index/')
        user = User.objects.get(username=username)
        item.status = 'during'
        item.maxPrice = amount
        item.winner = user
        item.voteDate = now
        item.save()
        messages.success(request, 'Przedmiot zlicytowany!')
        return HttpResponseRedirect('/index/')

