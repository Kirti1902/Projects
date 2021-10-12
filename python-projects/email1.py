import smtplib

s_email = (input("Enter the email id of sender:"))
r_email = (input("Enter the email id of reciver: "))
passw = (input(str("Enter your email id passord:")))


server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
server.ehlo()

server.login(s_email,passw)
print("Login Sucessfull")
subject=input("Enter the Subject of the body")
body= input("Enter the body part here:")
msg = "Subject:{}\n\n{}".format(subject,body)
server.sendmail(s_email,r_email,msg)
print("Message send successfully")
server.quit()
