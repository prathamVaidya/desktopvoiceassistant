import os
import tts
import webbrowser

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
    if len(cmd) > 0:
        if cmd[0] == "open":
            response = "Opening " + cmd[1]
            tts.say(response)
            webbrowser.open("https://" + cmd[1] + ".com")

            # try opening the program
            #os.system(cmd[1])
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
            tts.say("Searching for " + topic + " ...")

            import wikipedia
            # import pywhatkit
            # pywhatkit.search(topic)
            try:
                response = wikipedia.summary(topic, sentences=2)
                tts.say("Here is what I found,")
            except wikipedia.DisambiguationError as error:
                # api bug gives wrong defination try explain bird . Possibly parser issue
                response = "Well, can you be precise? " + str(error)
            except Exception as error:
                response = "Something went wrong. Error! " + str(error)
                print("...")
            tts.say(response)



    else:
        print("")




