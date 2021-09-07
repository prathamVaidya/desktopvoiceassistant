import speech_recognition as sr


# todo::
# - change function name to listen, call is misleading to other programmer.
# - use this wake_world variable for wake world.
# try not to use Hello Nova because when using other commands it will be very long
# you can use hello nova as greeting msg and just return a command "hello" which is handled in commands.py

wake_word = "nova"


def call():   # It takes microphone input from the user and returns string output
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # Using google for voice recognition.
            arr = command.lower().split()
            if 'hello' == arr[0] and 'nova' == arr[1]:  # The command should start with "Hello Nova"...
                arr.pop(0)  # removes first word HELLO
                arr.pop(0)  # removes second word NOVA
                print(" ".join(arr))
            elif 'thank you' in command:
                return print('okay bye!')
            else:
                call()

    except Exception as error:
        # Handle exceptions
        print('Exception -> ' + str(error))
        print('Please speak again...')  # This will be printed in case of improper voice or some mic issue
        call()
        pass


call()
