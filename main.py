from time import gmtime, sleep
from json import dump
from Users import Login_To_Account, clear

# checking for existing the user
UserName = Login_To_Account()

# terminal clearing
clear()

# the information of chats
user_inputs = {"text": "", "time": "", "day": "", "month": "", "year": ""}

while True:
    try:
        # saving chats
        message_file = open("./server/data.json", "a+")
        # start sending message
        text_input = input(f'{UserName}: ')
        # the information of chat such as text, time, etc
        user_inputs["text"] = text_input
        Chat_Time = gmtime()
        user_inputs["time"] = f'{Chat_Time.tm_hour}:{Chat_Time.tm_min}'
        user_inputs["day"], user_inputs["month"], user_inputs["year"] = Chat_Time.tm_mday, Chat_Time.tm_mon, Chat_Time.tm_year
        # sending information to text file
        dump(user_inputs, message_file)
        message_file.write('\n')
        message_file.close()
    except:
        print("Exit!")
        message_file.close()
        exit()
