from django.shortcuts import render 
from yahoo_fin.stock_info import *
from django.http.response import HttpResponse

import time

def stockPicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request,'mainapp/stockpicker.html',{'stock_picker':stock_picker})
# Create your views here.

def stockTracker(request):
    stockpicker = request.GET.getlist('stock_picker')
    print(stockpicker)
    data={} 
    available_stocks = tickers_nifty50()

    for i in stockpicker:
        if i not in available_stocks:
            return HttpResponse("ERROR")
    start= time.time()    
    print(start)    
    for i in stockpicker:
        details = get_quote_table(i)
        data.update({i:details})
    end=time.time() 
    time_taken =end - start
    print("time",time_taken)
    
    
    print(data)


    return render(request,'mainapp/stocktracker.html')
