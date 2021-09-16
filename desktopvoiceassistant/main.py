import stt
import tts
import commands
while True:
    print("listening...")
    text = stt.listen()
    if isinstance(text, int):
        tts.say("Error Occurred")
    else:
        commands.command(text)
