import smtplib
import getpass

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='ayushi65629@@gmail.com'
reciever='official.ayushi.singh@gmail.com'
msg="hii"
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,reciever,msg)
print("msg sent successfully")
s.quit()