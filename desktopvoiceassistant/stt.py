import speech_recognition as sr


# todo::
# - use this wake_word variable for wake world.
# you can use hello nova as greeting msg and just return a command "hello" which is handled in commands.py

wake_word = "nova"


def listen():   # It takes microphone input from the user and returns string output
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # Using google for voice recognition.
            arr = command.lower().split()
            if arr[0] == wake_word:  # The command should start with "Nova"...
                arr.pop(0)  # removes first word NOVA
                print(" ".join(arr))
            elif 'thank you' in command:
                return print('Okay Bye!')
            else:
                listen()

    except Exception as error:
        # Handle exceptions
        print('Exception -> ' + str(error))
        print('Please speak again...')  # This will be printed in case of improper voice or some mic issue
        listen()
        pass
    
   
