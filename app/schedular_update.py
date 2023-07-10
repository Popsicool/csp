import csv
from datetime import date, datetime, time
from django.conf import settings
from django.core.mail import EmailMessage


def update_something():
    print(datetime.now())
    # months = str(date.today()).split("-")[1]
    # day = str(date.today()).split("-")[2]
    # birthdays = []
    # with open("app/alumni.csv", "r") as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         mon = row[8].split("-")[0]
    #         if mon == months and row[8].split("-")[1] == day:
    #             obj = {}
    #             obj["name"] = row[3]
    #             obj["gender"] = row[6]
    #             obj["email"] = row[1]
    #             birthdays.append(obj)
    # if len(birthdays) > 0 :
    #     celebrants = "Today's birthday celebrants are\n"
    #     for celeb in birthdays:
    #         celebrants += celeb['name'] + " "
    #         text = f"Dear {celeb['name']},\n\nWe wish you a very happy birthday. Our prayer for you today is that the Lord grant you all your desires and answer all your prayers\nWe love you, and we celebrate you.\n\nCCCSP Funaab Alumni Body"
    #         email_subject = f'Happy Birthday {celeb["name"]}'
    #         email= EmailMessage(subject=email_subject,body=text, from_email= settings.EMAIL_FROM_USER,to=[celeb['email']])
    #         email.send()
    #     email_subject = 'Birthday Alert'
    #     email= EmailMessage(subject=email_subject,body=celebrants, from_email= settings.EMAIL_FROM_USER,to=[settings.EMAIL_FROM_USER])
    #     email.send()
