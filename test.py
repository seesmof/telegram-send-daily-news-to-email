import smtplib

sender = 'seesmwork@gmail.com'
receiver = 'seesmwork@gmail.com'
password = 'p0zBE5e146898992'
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(sender, password)
print("Login successful")
server.sendmail(sender, receiver, message)
print("Email sent successfully")
