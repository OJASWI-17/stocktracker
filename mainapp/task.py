from celery import shared_task
from threading import Thread
import yfinance as yf

def fetch_stock_data(ticker, data):
    """Function to fetch stock data using yfinance"""
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

@shared_task(bind=True)
def update_stock(self, selected_stocks):
    """Celery task to fetch stock data with threading"""
    data = {}
    threads = []

    # Create and start a thread for each stock ticker
    for ticker in selected_stocks:
        thread = Thread(target=fetch_stock_data, args=(ticker, data))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return data  
