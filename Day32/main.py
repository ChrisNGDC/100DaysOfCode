import smtplib
import datetime as dt
import random as r
import pandas as p
import os
from env_var import define_env
define_env()

mail = os.getenv("mail")
password = os.getenv("password")


def send_mail(name, email):
    with open(f'./letter_templates/letter_{r.randint(1,3)}.txt') as letter_file:
        letter = letter_file.read().replace('[NAME]', name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=mail, password=password)
        conn.sendmail(from_addr=mail, to_addrs=email, msg='Subject: Happy Birthday!!!\n\n' + letter)


now = dt.date.today()
today = now.month, now.day
birthdays = p.read_csv('./birthdays.csv')
birthdays_dict = {}
for (index, row) in birthdays.iterrows():
    birthdate = row.month, row.day
    if not birthdays_dict.get(birthdate):
        birthdays_dict[birthdate] = [row]
    else:
        birthdays_dict[birthdate].append(row)

for birthday in birthdays_dict:
    if birthday == today:
        for people in birthdays_dict[birthday]:
            send_mail(people['name'], people['email'])
