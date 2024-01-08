from django.shortcuts import render
import csv
from datetime import date
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, "index.html")

def celeb(request):
    months = str(date.today()).split("-")[1]
    birthdays = []
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
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
    return JsonResponse({"birthdays" : sorted_birthday})

def today(request):
    months = str(date.today()).split("-")[1]
    day = str(date.today()).split("-")[2]
    birthdays = []
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            mon = row[8].split("-")[0]
            if mon == months and row[8].split("-")[1] == day:
                obj = {}
                obj["name"] = row[3]
                obj["gender"] = row[6]
                obj["day"] = row[8].split("-")[1]
                birthdays.append(obj)
    sorted_birthday = sorted(birthdays, key= lambda x: x["day"])
    return JsonResponse({"birthdays" : sorted_birthday})