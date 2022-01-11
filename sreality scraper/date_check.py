import mysql.connector as mc
from mysql.connector import Error
from datetime import date, datetime, timedelta

today = datetime.now().date()

try:
    connection = mc.connect(host='127.0.0.1',
                            database='omega',
                            user='root',
                            password='root')
    '''
    connection = mc.connect(host='35.242.240.54',
                            database='central_log',
                            user='vitek',
                            password='devartrulezz')
    '''

    if (connection.is_connected()):
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        data = (today, 'https://www.test.test/')
        sql = ("INSERT INTO NewTable "
               "(date, url) "
               "VALUES (%s, %s)")
        cursor.execute(sql, data)

        sql = "SELECT * FROM NewTable WHERE url = %s"
        data = ('https://www.test.test/', )
        cursor.execute(sql, data)

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
