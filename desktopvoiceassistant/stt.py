import speech_recognition as sr


def call():   # It takes microphone input from the user and returns string output
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # Using google for voice recognition.
            arr = command.lower().split()
            if 'hello' == arr[0] and 'nova' == arr[1]:  # The command should start with "Hello Nova"...
                arr.pop(0)
                arr.pop(0)
                print(" ".join(arr))
            elif 'thank you' in command:
                return print('okay bye!')
            else:
                call()

    except:
        print('Please speak again...')  # This will be printed in case of improper voice or some mic issue
        call()
        pass


call()
