from django.shortcuts import render
import yfinance as yf
from threading import Thread

def stockPicker(request):
    # Hardcoded list of Nifty 50 tickers
    stock_picker = [
        'ADANIENT.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJFINANCE.NS',
        'BAJAJFINSV.NS', 'BPCL.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS', 'CIPLA.NS',
        'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GRASIM.NS',
        'HCLTECH.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS',
        'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'IOC.NS',
        'ITC.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS',
        'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS',
        'SBILIFE.NS', 'SHREECEM.NS', 'SBIN.NS', 'SUNPHARMA.NS', 'TATAMOTORS.NS',
        'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS',
        'UPL.NS', 'WIPRO.NS', 'ZEEL.NS'
    ]
    return render(request, 'mainapp/stockpicker.html', {'stock_picker': stock_picker})

def fetch_stock_data(ticker, data):
    """Helper function to fetch stock data using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        details = stock.info  # Get all available stock info

        # Extract the required fields
        data[ticker] = {
            'current_price': details.get('currentPrice', 'N/A'),
            'previous_close': details.get('previousClose', 'N/A'),
            'volume': details.get('volume', 'N/A'),
            'market_cap': details.get('marketCap', 'N/A'),
            'open_price': details.get('open', 'N/A'),
            'day_high': details.get('dayHigh', 'N/A'),
            'day_low': details.get('dayLow', 'N/A'),
        }
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        data[ticker] = {
            'error': f"Failed to fetch data for {ticker}"
        }

def stockTracker(request):
    # Get the selected stocks from the request
    selected_stocks = request.GET.getlist('stock_picker')  # Get all selected stocks

    # Dictionary to store stock data
    data = {}

    # Create a list to hold thread objects
    threads = []

    # Create and start a thread for each stock
    for ticker in selected_stocks:
        thread = Thread(target=fetch_stock_data, args=(ticker, data))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Pass the data to the template
    return render(request, 'mainapp/stocktracker.html', {'data': data})