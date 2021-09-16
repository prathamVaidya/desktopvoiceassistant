import speech_recognition as sr
import tts

# todo::
# - use this wake_word variable for wake world.
# you can use hello nova as greeting msg and just return a command "hello" which is handled in commands.py

wake_word = "nova"


def listen():   # It takes microphone input from the user and returns string output
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # Using google for voice recognition.
            arr = command.lower().split()
            if arr[0] == wake_word:  # The command should start with "Nova"...
                arr.pop(0)  # removes first word NOVA
                result = " ".join(arr)
                print("User: "+result)
                return result
            elif arr[0] == "goodbye" and arr[1] == wake_word:
                tts.say("Good Bye, Have a nice day!")
                exit()
            else:
                return listen()

    except Exception as error:
        # Handle exceptions

        if str(error) != "":
            print('Exception -> ' + str(error))
            return error.errno

        else:
            # print('...')  # This will be printed in case of improper voice or some mic issue
            return listen()
            pass


