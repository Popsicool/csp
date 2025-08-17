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
    months = int(str(date.today()).split("-")[1])
    birthdays = []
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            mon = int(row[5].split("/")[0])
            if mon == months:
                obj = {}
                obj["name"] = row[2]
                obj["gender"] = row[3]
                obj["day"] = row[5].split("/")[1]
                birthdays.append(obj)
    sorted_birthday = sorted(birthdays, key= lambda x: x["day"])
    return JsonResponse({"birthdays" : sorted_birthday})

def mail_celeb(request):
    months = int(str(date.today()).split("-")[1])
    day = int(str(date.today()).split("-")[2])
    birthdays = []
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            mon = int(row[5].split("/")[0])
            if mon == months and int(row[5].split("/")[1]) == day:
                birthdays.append(row)
    for row in birthdays:
        email = row[1]
        name = row[2].title()
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
    months = int(str(date.today()).split("-")[1])
    day = int(str(date.today()).split("-")[2])
    birthdays = []
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            mon = int(row[5].split("/")[0])
            if mon == months and int(row[5].split("/")[1]) == day:
                obj = {}
                obj["name"] = row[2]
                obj["gender"] = row[3]
                obj["day"] = row[5].split("/")[1]
                birthdays.append(obj)
    sorted_birthday = sorted(birthdays, key= lambda x: x["day"])
    return JsonResponse({"birthdays" : sorted_birthday})

def mail(request):
    with open("app/alumni.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        # reader = [["aaa","akinolasamson1234@gmail.com", "abc", "OLADIMEJI Martins Ayomikun"]]
        for row in reader:
            email = row[1]
            name = row[2].title()
            subject = "🎉 Let’s Reconnect! CCCSP FUNAAB Alumni Hangout Coming Soon"
            html_message = f"""
            <p>Good evening <strong>{name}</strong>,</p>

            <p>We hope this message finds you well.</p>

            <p>
            The <strong>CCCSP FUNAAB Alumni body</strong> is excited to invite you to our upcoming <strong>General Hangout</strong> — 
            a special time of love, laughter, and reconnection. It’s that moment we all gather again as one family, 
            to catch up with our “long time, no see” friends, and relive the joy of our days at FUNAAB.
            </p>

            <p>
            Expect a beautiful atmosphere filled with fellowship, fun activities, and those unforgettable CCCSP songs 
            and our beloved FUNAAB anthem that remind us we never truly left.
            </p>

            <p>📅 <b>Date:</b> A Saturday and Sunday in October (exact date to be confirmed)<br>
            📍 <b>Venue:</b> Abeokuta — our home ground where the memories began</p>

            <p>Your presence means a lot to us, and we can’t wait to see you there. Let’s make this a reunion to remember!</p><br>

            <p>
            <a href="https://docs.google.com/forms/d/1sLAUDBQ_THqtex2FHDC8o2PDPgkpQ0k2YpkkUHPsWu0/viewform"
            style="background-color:#4CAF50;color:white;padding:10px 20px;text-decoration:none;border-radius:6px;">
            👉 Register Here
            </a>
            </p>
            <br>

            <p>With love,<br>
            CCCSP FUNAAB Alumni Family</p>
            """

            email = EmailMessage(
                subject,
                html_message,
                settings.EMAIL_FROM_USER,
                to=[email]
            )
            email.content_subtype = "html"  # 👈 makes it send as HTML
            email.send()
            # email_message = EmailMessage(
            #     subject=subject,
            #     body=message,
            #     from_email=settings.EMAIL_FROM_USER,
            #     to=[email]  # Use the recipient's email here
            # )
            try:
                email.send()
                # email_message.send()
                print(f"Email sent to {name} ({email})")
            except Exception as e:
                print(f"Failed to send email to {name} ({email}): {e}")
            time.sleep(1)

    return render(request, "index.html")
