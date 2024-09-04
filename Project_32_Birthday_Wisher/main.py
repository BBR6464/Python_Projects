import smtplib
import datetime as d
import random

MY_EMAIL = "mbmalik8859@gmail.com"
MY_PASSWORD = "hoxiefsxmbmygsed"

now = d.datetime.now()
day = now.weekday()

if day == 2:  # Monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()  # Corrected to read all lines
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # Added port number
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
