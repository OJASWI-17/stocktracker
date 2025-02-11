from django.shortcuts import render ,HttpResponse
from yahoo_fin.stock_info import *


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
    for i in stockpicker:
        details = get_quote_table(i)
        data.update({i:details})


    print(data)


    return render(request,'mainapp/stocktracker.html')
