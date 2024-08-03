import google_bot
import speech_recognizer as sr
import talk_back as tb

print("Welcome to the google bot!")
duration = 5

if input("Shall I start recording [y]es or [n]o: ").lower() == "y":
    sr.record_audio("output.wav", duration)
    search_text = sr.recognize_speech("output.wav")
    tb.text_to_audio(f"Ok, I will search {search_text}")
    tb.play()
    google_bot.google_search(search_text)
else:
    print("Alright, Bye!")
