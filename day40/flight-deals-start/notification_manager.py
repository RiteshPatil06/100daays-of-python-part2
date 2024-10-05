import os
import smtplib

from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_AUTH_TOKEN'])
        self.connection = smtplib.SMTP(os.environ['SMTP_ADDRESS'])
        self._email = os.environ['MY_EMAIL']
        self._password = os.environ['PASSWORD']
        self._smtp_address = os.environ['SMTP_ADDRESS']

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_="+1 717 276 0228",
            body=message_body,
            to="+918767883223"
        )
        #Print if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self._email, self._password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self._email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8'))
