import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='sales_db',
            user='root',
            password='your_password' # replace your_password with your own password
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
