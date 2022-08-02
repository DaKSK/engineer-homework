This project was created using Python 3.10.4
To store the data I used Oracle Instant Client and the Oracle Python package cx_Oracle
I created a free tier Oracle Cloud database and connected to it using the wallet
I used dotenv to store the credentials and load them into the environment

I knew of a public stocks API www.alphavantage.co for which I got a API key so I used that to get the AAPL stock data

I would've preferred to use an ORM but since I didn't know how to connect SQLAlchemy to Oracle I used the cx_Oracle package and SQL strings
Once I had the connection set up, it was relatively straight forward to add the data to the database
I interpreted the worst and best stock day as being the highest and the lowest stock close price

To create the plot I used the basic matplotlib. Previously I've played around with Streamlit to create a webapp with a dashboard, so this was familiar to me.