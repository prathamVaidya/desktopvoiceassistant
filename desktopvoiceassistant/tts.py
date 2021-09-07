import os
import playsound

# Constants
AUDIO_FILE = "temp.wav"
GOOGLE_TTS = 1
MOZILLA_TTS = 2


def say(text, speed=False, tts_name=GOOGLE_TTS):
    print(text)
    if tts_name == GOOGLE_TTS:
        # Use gTTS for Text to Speech. Internet Required.
        from gtts import gTTS

        tts = gTTS(text, slow=speed)
        tts.save(AUDIO_FILE)
        playsound.playsound(AUDIO_FILE, True)
        os.system("rm " + AUDIO_FILE)

    elif tts_name == MOZILLA_TTS:
        # Use Mozilla TTS with Tacotron-2

        # Todo: Implement this
        print("Not Available")

