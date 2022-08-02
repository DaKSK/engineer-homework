'''
use public REST API to get financial historic data about AAPL stocks
store it in Oracle database
generate a report from stored data:
-> amount of stored data
-> worst stock day
-> best stock day
-> draw a chart
'''

import os
import cx_Oracle
from dotenv import load_dotenv
import requests
import json
import matplotlib.pyplot as plt


load_dotenv()


# get data from API
alpha_api = os.environ.get("API_KEY")
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey={alpha_api}'
response = requests.get(url)
data = json.loads(response.text)

# Establish connection to Oracle database

USER = os.environ.get('USER')
PASSWORD = os.environ.get("PASSWORD")
TNS = os.environ.get("TNS")
connection = cx_Oracle.connect(USER, PASSWORD, TNS)
cursor = connection.cursor()

# # create table
cursor.execute("""
CREATE TABLE stocks (
    time DATE,
    open NUMBER,
    high NUMBER,
    low NUMBER,
    close NUMBER,
    volume NUMBER
)
""")

# # insert data into table
for key, value in data['Time Series (Daily)'].items():
    cursor.execute("""
    INSERT INTO stocks (time, open, high, low, close, volume)
    VALUES (to_date(:time, 'YYYY-MM-DD'), :open, :high, :low, :close, :volume)
    """,
    time=key,
    open=value['1. open'],
    high=value['2. high'],
    low=value['3. low'],
    close=value['4. close'],
    volume=value['5. volume']
    )

# commit changes
connection.commit()

# generate a report

# amount of stored data
cursor.execute('SELECT COUNT(*) FROM stocks ')
print('Amount of stored data:', cursor.fetchone()[0])

# worst stock day
cursor.execute("SELECT to_char(time, 'YYYY-MM-DD'), close FROM stocks  WHERE close = (SELECT MIN(close) FROM stocks )")
print('Worst stock day:', cursor.fetchone())

# best stock day
cursor.execute("SELECT to_char(time, 'YYYY-MM-DD'), close FROM stocks  WHERE close = (SELECT MAX(close) FROM stocks )")
print('Best stock day:', cursor.fetchone())

# draw a chart
cursor.execute("SELECT to_char(time, 'YYYY-MM-DD'), close FROM stocks ORDER BY time ASC")
x = []
y = []
for row in cursor:
    x.append(row[0])
    y.append(row[1])

plt.plot(x, y)
plt.xticks(rotation=45)
plt.ylabel('Price')
plt.xlabel('Date')
plt.title('AAPL')
plt.show()

# close connection
cursor.close()
connection.close()