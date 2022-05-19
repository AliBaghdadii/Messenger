"""
Messenger 1.1
Created by Ali Baghdadi
No Copyright
"""
from json import dump
from time import localtime, strftime

# creating text file
message_file = open("data.json", "a+")

# where messages save
user_inputs = dict()

def getting_message(user_inputs):
    try:
        # getting message
        text_input = input("Enter your message: ")
        user_inputs["text"] = text_input
        # describe the time the message sent
        user_inputs["time"] = strftime("%a, %d %b %Y %H:%M", localtime())
        # if user wants to leave
        if text_input.lower() == "exit":
            print("you left")
            message_file.close()
            exit()
        # sending messages to text file
        dump(user_inputs, message_file)
        # message_file.write(';\n')
        # message_file.write(str(user_inputs["text"] + "\n"))
        # message_file.write(str(user_inputs["time"] + "\n"))
        # message_file.write("\n")
    # if input has error
    except:
        print("Program closed.")
        message_file.close()
        exit()


while True:
    getting_message(user_inputs)
