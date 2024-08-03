import time
from gtts import gTTS
import pygame
import os


def text_to_audio(text):
    language = "en"

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")


def play():
    try:
        pygame.mixer.quit()
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")
    except Exception as e:
        print(f"Error in play: {e}")


if __name__ == "__main__":
    text_to_audio("Google bot is nice.")
    play()
