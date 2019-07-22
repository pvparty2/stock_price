# Your personal information which you should keep secret is used here
import smtplib

class Messenger():
    def __init__(self):
        """Initialize a messenger."""
        self.email = 'your_email'
        
        # Gmail requires separate password
        self.passw = 'your_password'
        
        # the address is unique for each mobile carrier
        self.recipient = 'your_number@tmomail.net'


    def send_text_msg(self, e_subject, e_body):
        """Send a text message of the stock name and stock price."""
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

        smtp_obj.starttls()
        smtp_obj.login(self.email, self.passw)

        # Send text message of stock price and name
        message = ('From: %s\r\n' % self.email
                   + 'To: %s\r\n' % self.recipient
                   + 'Subject: %s\r\n' % e_subject
                   + '\r\n'
                   + e_body)

        smtp_obj.sendmail(self.email, self.recipient, message)
        smtp_obj.quit()


    
