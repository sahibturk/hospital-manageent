import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",   # MySQL username
        password="191892turk",  # MySQL password
        database="HospitalDB"
    )
