##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
#
# 2. Check if today matches a birthday in the birthdays.csv
#
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#
# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import os
import pandas
now = dt.datetime.now()
from random import choice
data = pandas.read_csv("./birthdays.csv")
MY_EMAIL = ""
MY_PASSWORD = ""
def happy_birthday(name, email):
    arr = os.listdir('C:/Users/noureldine/Desktop/snake/birthdayemail app/letter_templates')
    with open(f"./letter_templates/{choice(arr)}", "r") as letter_file:
        file_content = letter_file.read()
        updated_file = file_content.replace("[YOUR_NAME]", "Nour").replace("[NAME]", name)
        with smtplib.SMTP('smtp-mail.outlook.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(MY_EMAIL, MY_PASSWORD)
            smtp.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                          msg=f"Subject:HAPPY BIRTHDAY!\n\n{updated_file}")
            print("Email sent!")
for i in range(len(data)):
    current_month, current_day = now.month, now.day
    data_month, data_day = data["month"][i], data["day"][i]
    if current_month == data_month and current_day == data_day:
        happy_birthday(data["name"][i], data["email"][i])


