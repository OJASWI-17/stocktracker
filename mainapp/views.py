from django.shortcuts import render
import yfinance as yf

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

def stockTracker(request):
    # Fetch stock details for HDFCBANK.NS using yfinance
    ticker = 'HDFCBANK.NS'
    stock = yf.Ticker(ticker)
    details = stock.info  # Get all available stock info

    # Extract the required fields
    current_price = details.get('currentPrice', 'N/A')  # Current price
    previous_close = details.get('previousClose', 'N/A')  # Previous close
    volume = details.get('volume', 'N/A')  # Trading volume
    market_cap = details.get('marketCap', 'N/A')  # Market capitalization
    open_price = details.get('open', 'N/A')  # Open price
    day_high = details.get('dayHigh', 'N/A')  # Day's high
    day_low = details.get('dayLow', 'N/A')  # Day's low

    # Print the details for debugging
    # print(f"Details for {ticker}:")
    # print(f"Current Price: {current_price}")
    # print(f"Previous Close: {previous_close}")
    # print(f"Volume: {volume}")
    # print(f"Market Cap: {market_cap}")
    # print(f"Open Price: {open_price}")
    # print(f"Day's High: {day_high}")
    # print(f"Day's Low: {day_low}")

    # Pass the details to the template
    return render(request, 'mainapp/stocktracker.html', {
        'ticker': ticker,
        'current_price': current_price,
        'previous_close': previous_close,
        'volume': volume,
        'market_cap': market_cap,
        'open_price': open_price,
        # 'day_high': day_high,
        # 'day_low': day_low,
    })
