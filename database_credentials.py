import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

HOSTNAME = os.getenv('HOSTNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')

# # # # Connect to MySQL Database# # # #

mydb = mysql.connector.connect(
    host = HOSTNAME,
    user = USER,
    password = PASSWORD,
    database = DATABASE
)

cursor = mydb.cursor() #Name the cursor something simple for easier use
