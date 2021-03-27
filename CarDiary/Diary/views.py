from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, TO
from datetime import *
from django.utils import timezone
# Create your views here.


def index(request):

    return render(request, 'index2.html', {'Car': Car, 'TO': TO})
