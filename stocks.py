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

load_dotenv()

USER = os.environ.get('USER')
PASSWORD = os.environ.get("PASSWORD")
TNS = os.environ.get("TNS")

connection = cx_Oracle.connect(USER, PASSWORD, TNS)
