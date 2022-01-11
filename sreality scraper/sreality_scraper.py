import urllib.request
import json
import csv
from datetime import date, datetime, timedelta
import mysql.connector as mc
from mysql.connector import Error


def main():
    now = datetime.now()
    today = date.today()
    count = 0

    thisdict = {
        2: "1+kk",
        3: "1+1",
        4: "2+kk",
        5: "2+1",
        6: "3+kk",
        7: "3+1",
        8: "4+kk",
        9: "4+1",
        10: "5+kk",
        11: "5+1",
        12: "6-a-vice",
        16: "atypicky",
        33: "chata",
        35: "pamatka-jine",
        37: "rodinny",
        39: "vila",
        40: "na-klic",
        43: "chalupa",
        44: "zemedelska-usedlost",
        54: "undefined",  # nebo jako vicegeneracni-dum , až si seznam opraví chybu v url

    }
    try:
        '''
        connection = mc.connect(host='localhost',
                                            database='omega',
                                            user='root',
                                            password='root')
                                                '''
        connection = mc.connect(host='35.242.240.54',
                                database='central_log',
                                user='vitek',
                                password='devartrulezz')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            '''

            data = ('https://www.test.test/', "byt", today, today, 0)
            statement = ("INSERT INTO sreality "
                        "(url, typ, pridano, posledny_scan, import) "
                        "VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(statement, data)
                '''
        for category in range(1, 3):
            for page in range(1, 12):
                with urllib.request.urlopen("https://www.sreality.cz/api/cs/v2/estates?category_main_cb="+str(category)+"&category_type_cb=1&no_auction=1&per_page=999&page=" + str(page)) as url:
                    data = json.loads(url.read().decode())

                # print(data["_embedded"]["estates"])
                    for list in data["_embedded"]["estates"]:
                        type = list["seo"]["category_main_cb"]  # byt / dum
                        if (type == 1):
                            type = "byt"
                        else:
                            type = "dum"

                        location = list["seo"]["locality"]  # locality slug

                        description_number = list["seo"]["category_sub_cb"]
                        if (description_number in thisdict):
                            # search dictionary
                            # popisek bytu - 1+kk
                            description = thisdict[description_number]

                        link = (list["_links"]["self"]["href"]
                                ).split("/")[4]  # jen číslo
                        url = "https://www.sreality.cz/detail/prodej/" + \
                            type + "/" + description + "/" + location + "/" + link

                        sql = "SELECT * FROM sreality WHERE url = %s AND import = %s"
                        data = ("https://www.test.test/", 0)
                        cursor.execute(sql, data)

                        result = cursor.fetchall()
                        result_found = cursor.rowcount

                        if(result_found > 0):
                            # Update
                            print("rowcount: " + str(result_found))

                            for row in result:
                                if(row[3] < now-timedelta(days=30)):
                                    pass
                                    # lezak - prepsat do db a upravit col import
                                else:
                                    print("not older.")
                                    # fix this logic
                            data = (now, "https://www.test.test/")
                            statement = (
                                "UPDATE sreality SET  posledny_scan = %s WHERE url = %s")
                            cursor.execute(statement, data)

                        else:
                            # Create
                            data = (url, type, today, today, 0)
                            statement = ("INSERT INTO sreality "
                                         "(url, typ, pridano, posledny_scan, import) "
                                         "VALUES (%s, %s, %s, %s, %s)")
                            cursor.execute(statement, data)

                        count += 1
                    print(count)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.commit()
            connection.close()
            print("MySQL connection is closed")


main()

'''

with open('result.csv', 'a', encoding='UTF8', newline='') as f:
 writer = csv.writer(f)

 # write the header

 # write multiple rows
 writer.writerow(data)
'''
