from django.shortcuts import render
from .models import Today, Money
def home(request):

    today_objects = Today.objects.all()

    money_objects = Money.objects.all()

    return render(request, 'hello/home.html', {"today_list": today_objects,
                                               "money_list": money_objects, 
                                              } )
 

def received(request):

    return render(request, 'hello/received.html')

def remaining(request):

    return render(request, 'hello/remaining.html')

def sold(request):

    return render(request, 'hello/sold.html')