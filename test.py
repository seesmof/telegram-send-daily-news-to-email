import smtplib

email = 'seesmwork@gmail.com'
password = 'p0zBE5e146898992'

to_email = 'your_email@gmail.com'
message = 'Subject: {}\n\n{}'.format('Hi', 'Hello from Python!')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
server.sendmail(email, to_email, message)
server.quit()
