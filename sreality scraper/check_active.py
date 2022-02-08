import urllib.request
import json
import csv
from datetime import date, datetime, timedelta
import mysql.connector as mc
from mysql.connector import Error

count = 0

with open('check_active.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        if(count == 0):
            count = 1
            continue
        # process each line
        try:

            url = line[15]
            request = urllib.request.urlopen(url)

            print(request.getcode())
        except urllib.error.HTTPError as e:
            print("there was an Error: " + str(e.code) + "at url: " + url)
            quit
        else:
            print("this url works: " + url)

            with open('active_results.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)

                # write the header

                # write multiple rows
                writer.writerow(line)
