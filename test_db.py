import mysql.connector

try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root"
    )

    print("Connected Successfully!")

except Exception as e:
    print("Error:", e)