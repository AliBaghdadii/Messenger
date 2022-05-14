"""
Messenger 1.0
Created by Ali Baghdadi
No Copyright
"""

# creating text file
message_file = open("messages.txt", "w")


def getting_message():
    try:
        # getting message
        text_input = input("Enter your message: ")
        # if user wants to leave
        if text_input.lower() == "exit":
            exit()
        # sending messages to text file
        message_file.write(text_input)
    # if input has error
    except:
        print("Program closed.")
        exit()


while True:
    getting_message()
