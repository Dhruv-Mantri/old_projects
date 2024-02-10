import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = "dhruvmantripy@gmail.com"
password = "ALIcia12."

# emails = ["srminecraft247@gmail.com","OmVhatkarYTC@gmail.com","Soni.74.jha@gmail.com","tsnaveen@hotmail.com","anaykulks@gmail.com","harple2120@gmail.com","vibhasmadhwal@hotmail.com","Rayzray227@outlook.com","singhpk2@gmail.com","gayathri.kollu@gmail.com","rikbansal02@gmail.com","shruthirap@gmail.com","Madhumidhas@gmail.com","Littleandrew2009@gmail.com","Srinivasmusti@hotmail.com"]
# emails = ["srminecraft247@gmail.com", "singhpk2@gmail.com","gayathri.kollu@gmail.com", "mydiku2021@gmail.com"]
emails = ["mandhr908@gmail.com"]

for email_target in emails:
    receiver = email_target
    # name = input("What is their name?  ")

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(email, password)

    message = """Hello, 
    DISCORD BOT

    Google Meet link for today: https://meet.google.com/dkh-awqd-xah

    ~ Dhruv Mantri"""

    msg = MIMEMultipart()
    msg["From"] = email
    msg['To'] = receiver
    msg['Subject'] = "Python Intermediate Course 6/15"

    msg.attach(MIMEText(message, 'plain'))


    s.send_message(msg)
    del msg
    s.quit()

print("Messages sent.")