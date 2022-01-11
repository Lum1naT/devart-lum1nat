import mysql.connector as mc
from mysql.connector import Error

try:
    connection = mc.connect(host='35.242.240.54',
                            database='central_log',
                            user='vitek',
                            password='devartrulezz')
    if (connection.is_connected()):
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
