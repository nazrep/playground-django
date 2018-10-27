# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from time import strftime, localtime
import datetime

# Create your views here.




def index(request):
    # wyswietlic aktualna godzine HH:mm:ss i date
    return render(request, 'date.html', {
        'showtime': strftime("Today is %d-%m-%Y and the time is  %H:%M:%S", localtime())
    })