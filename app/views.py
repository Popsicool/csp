from django.shortcuts import render
import csv
from datetime import date
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
import time

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

def mail_celeb(request):
    months = str(date.today()).split("-")[1]
    day = str(date.today()).split("-")[2]
    birthdays = []
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            mon = row[8].split("-")[0]
            if mon == months and row[8].split("-")[1] == day:
                birthdays.append(row)
    for row in birthdays:
        email = row[1]
        name = row[3].title()
        subject = f"Happy Birthday, {name}"
        message = f"""Dear {name},\n\nHappy Birthday! 🎂✨\n\nToday, we celebrate the wonderful gift that you are to our community and the world. Your kindness, faith, and dedication to God’s work inspire us all.\n\n“This is the day that the Lord has made; let us rejoice and be glad in it.” – Psalm 118:24\n\nAs you mark another year of God’s goodness, may you feel His boundless love and blessings surrounding you. We pray that this new year of your life is filled with:\n\tJoy that overflows\n\tPeace that surpasses understanding\n\tStrength for every challenge\n\tGrace for every step\n\tAnd love beyond measure\n\nMay your light continue to shine brightly, reflecting God’s glory in all that you do. Thank you for being such a blessing to our community!\n\nEnjoy your special day to the fullest—it's all about celebrating YOU and the amazing plans God has in store for your life. 🎉\n\nIn Christ's love,\nCCCSP FUNAAB ALUMNI REP\n+2347035570512"""
        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_FROM_USER,
            to=[email]
        )
        try:
            email_message.send()
            print(f"Email sent to {name} ({email})")
        except Exception as e:
            print(f"Failed to send email to {name} ({email}): {e}")
        time.sleep(1)
    return render(request, "index.html")

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

def mail(request):
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[1]
            name = row[3].title()
            subject = "Happy New Year from CCCSP FUNAAB ALUMNI BODY !"
            message = f"""Dear {name},\n\nHappy New Year! 🎆\n\nAs we step into 2025, we are filled with gratitude for the blessings of the past year and the joy of having you as part of our community. Your love, prayers, and dedication to CCCSP Funaab have been a beacon of hope and inspiration.\n\n“For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future.” – Jeremiah 29:11\n\nAs we embrace the new year, we are reminded of God’s faithfulness and the endless possibilities He places before us. Let us continue to seek His guidance, love one another deeply, and shine His light in all we do.\n\nWe pray that this year brings you and your loved ones abundant blessings, strengthened faith, and countless moments of joy and peace.\n\nThank you for being a vital part of our family in Christ. Together, let us make 2025 a year of purpose, impact, and growth in His Kingdom.\n\nIn Christ's love,\nCCCSP FUNAAB ALUMNI REP\n+2347035570512
            """
            email_message = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_FROM_USER,
                to=[email]  # Use the recipient's email here
            )
            try:
                # email_message.send()
                print(f"Email sent to {name} ({email})")
            except Exception as e:
                print(f"Failed to send email to {name} ({email}): {e}")
            time.sleep(1)

    return render(request, "index.html")
