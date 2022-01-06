import urllib.request
import json
import csv
from datetime import date

today = date.today().strftime("%d.%m.%Y")
count = 0
for main in range(1, 3):
    for page in range(1, 12):
        with urllib.request.urlopen("https://www.sreality.cz/api/cs/v2/estates?category_main_cb="+str(main)+"&category_type_cb=1&no_auction=1&per_page=999&page=" + str(page)) as url:
            data = json.loads(url.read().decode())

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

        # print(data["_embedded"]["estates"])
            for list in data["_embedded"]["estates"]:
                type = list["seo"]["category_main_cb"]  # byt / dum
                if (type == 1):
                    type = "byt"
                else:
                    type = "dum"

                location = list["seo"]["locality"]  # locality slug
                # popisek bytu - 1+kk
                description_number = list["seo"]["category_sub_cb"]
                if (description_number in thisdict):
                    # search dictionary
                    description = thisdict[description_number]

                link = (list["_links"]["self"]["href"]
                        ).split("/")[4]  # jen číslo
                # print(link.split("/")[4])
                url = "https://www.sreality.cz/detail/prodej/" + \
                    type + "/" + description + "/" + location + "/" + link
                # print(url)
                header = ['date', 'url']
                data = [today, url]

                with open('result.csv', 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)

                    # write the header

                    # write multiple rows
                    writer.writerow(data)

                count += 1
            print(count)
