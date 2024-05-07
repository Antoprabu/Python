import requests
import datetime
import json

# Your Alpha Vantage API key
api_key = 'VHVQAC0RA9YB85QK'

# Get the current month and year
current_month = datetime.date.today().strftime('%Y-%m')

url = 'https://www.alphavantage.co/query?function=TOURNAMENT_PORTFOLIO&season=2023-04&apikey=VHVQAC0RA9YB85QK'
r = requests.get(url)
data = r.json()

print(data)
