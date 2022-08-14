from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from tradeMonitor.forms import Stock
from . import service

# Create your views here.
def index(request):
    if request.method == 'POST':
        print("done")
        symbol=request.POST.get("stocksym")
        print(symbol)
        response=service.getData(symbol)
        return render(request,'index.html',response)
    else:
        return render(request,"index.html")