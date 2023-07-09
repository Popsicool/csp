import csv
from datetime import date
from tabulate import tabulate

months = str(date.today()).split("-")[1]


birthdays = []
with open("alumni.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        mon = row[8].split("-")[0]
        if mon == months:
            obj = {}
            obj["name"] = row[3]
            obj["gender"] = row[6]
            obj["day"] = row[8].split("-")[1]
            birthdays.append(obj)

sorted_birthday = sorted(birthdays, key= lambda x: x["day"])
print(tabulate(sorted_birthday))