import yagmail

from_email = 'seesvalorant@gmail.com'
to_email = 'seesmwork@gmail.com'
password = ',X)kC9-)}svS"n_d'

yag = yagmail.SMTP(from_email, password)
yag.send(to=to_email, subject="Hi",
         contents="Hello, this is a test email from Python!")
