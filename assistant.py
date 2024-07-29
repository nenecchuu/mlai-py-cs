import os
import random

from smtplib import SMTP
from schedule.schedule import Schedule

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Assistant():
    def __init__(self):
        self.schedule = []
        self.name = ''
        self.email = ''

        pass

    def setName(self, name: str):
        self.name = name
        print("Name changed to: " + name)
        return self

    def printName(self):
        print("My name is: " + self.name)

    def createSchedule(self, name: str):
        s = Schedule().withName(name)
        self.schedule.append(s)

    def printSchedule(self):
        if (len(self.schedule)  == 0):
            print("No schedule")
        else:
            print("Your schedule:")
            for s in self.schedule:
                date = s.date.date().isoformat()
                print("[" + date + "]" + " " + s.name)

    def printRandomJoke(self):
        jokes = (
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What do you call fake spaghetti? An impasta!",
            "Why did the bicycle fall over? Because it was two-tired!"
        )
        print(random.choice(jokes))

    def sendEmail(self, receiver, subject, body):
        smtp_email = os.getenv('SMTP_EMAIL')
        smtp_password = os.getenv('SMTP_PASSWORD')

        try:
            message = MIMEMultipart()
            message['From'] = self.name
            message['To'] = receiver
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            with SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(smtp_email, smtp_password)
                server.send_message(message)
                print('Email sent successfully')
        except Exception as e:
            print(f'Error sending email: {e}')