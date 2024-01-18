#send mail to multiple mailid 
#import smtp lib and call it using alias
import smtplib as s

#initialise an object and call 's' class
#add server SMTP ("server_name",portnumber) 
#portnumber of gmail is 587
obj = s.SMTP("smtp.gmail.com",587)

#methods ehlo and starttls
obj.ehlo()
obj.starttls()

#login method login("mail_id","password")
obj.login("usermailid@gmail.com","password")
subject = "Testing"
body = "Hello,This is a test message"
#message of the mail , subject+body used format specifiers
message = "subject : {}\n\n{}".format(subject,body)

#list of mail address to send the email
list_add = ["user1@gmail.com",
            "user2@gmail.com",
            "user3@gmail.com"]

#send mail method obj.sendmail("mailid",list_address,message)
obj.sendmail("usermailid@gmail.com",list_add,message)

print("send mail")
#quit is used to close the server
obj.quit()
