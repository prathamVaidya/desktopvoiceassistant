import os
import tts


# Commands
# open <APP>, open chrome, open notepad
# say <TO_BE_REPEATED>, say Daddy
# explain <ANYTHING>, explain computer, explain iphone
# (A lot of words not working for some reason, hat gives cat results)
# time

greetings_msg = "HI, I am NOVA, your virtual assistant. " \
                "I can help you with many things. Try to say NOVA, explain ARTIFICIAL INTELLIGENCE"


def command(cmd_str):
    print("--------------------------------------------------")
    cmd = cmd_str.split()
    # handle text command. Arg[]: cmd Array[] of words in commands
    if cmd[0] == "open":
        response = "Opening "+cmd[1]
        tts.say(response)

        # try opening the program
        os.system(cmd[1])
    elif cmd[0] == "speak" or cmd[0] == 'repeat' or cmd[0] == 'say':
        # repeat user statement
        sub_cmd = cmd
        sub_cmd.pop(0)
        response = " ".join(sub_cmd)
        tts.say(response)
    elif cmd[0] == "explain":
        # explain anything
        sub_cmd = cmd
        sub_cmd.pop(0)
        topic = " ".join(sub_cmd)
        tts.say("Searching for " + topic+" ...")

        import wikipedia

        try:
            response = wikipedia.summary(topic, sentences=3)
            tts.say("Here is what I found,")
        except wikipedia.DisambiguationError as error:
            # api bug gives wrong defination try explain bird . Possibly parser issue
            response = "Well, can you be precise? "+str(error)
        except Exception as error:
            response = "Something went wrong. Error! "+str(error)

        tts.say(response)

    elif cmd[0] == "time":
        # shows time
        import time
        localTime = time.localtime(time.time())

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

        date = str(localTime.tm_mday)+ " " + str(months[localTime.tm_mon-1])+ " " + str(localTime.tm_year)
        tts.say("Today is "+date)

        if localTime.tm_hour > 12:
            hour = str(localTime.tm_hour - 12) + 'am'
        else:
            hour = str(localTime.tm_hour) + 'pm'

        time = hour + " " + str(localTime.tm_min) + " minutes"
        tts.say("and time is " + time)

    elif cmd[0] == "hello":
        tts.say(greetings_msg)
    elif cmd[0] == "goodbye":
        tts.say("Good Bye, Have a nice day!")
        exit()
    else:
        tts.say("I didn't get that")

    print("--------------------------------------------------")



