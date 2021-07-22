from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, TO
from datetime import *
from django.utils import timezone
# Create your views here.
#test

def index(request):
    currentcar = Car.objects.get(pk=1)
    toforcar = TO.objects.all()
    last = TO.objects.last()
    print(last.mileage)





    return render(request, 'index2.html', {'Car': Car, 'TO': TO, 'currentcar': currentcar,'toforcar': toforcar,'last': last})
