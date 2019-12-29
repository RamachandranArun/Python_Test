'''dob=['12mar','10oct','28dec','20dec']
name=['Raj','Arun','Raja','kumar']
emailid=['raj@gmail.com','Arun@gmail.com','ja@gmail.com','k@gmail.com']
value=input('Enter the dob : ')
for i in range (len(dob)):
    if dob[i]==value:
        print('Hi',name[i],'Happy birthday to',emailid[i],'on',dob[i])'''
# email sending
import smtplib
pwd=input('Enter your pwd : ')
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('hirarun@gmail.com',pwd)
s.sendmail('hirarun@gmail.com','hirarun@yahoo.com','hi test')
s.quit
