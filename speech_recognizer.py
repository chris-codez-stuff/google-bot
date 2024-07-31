import sounddevice
import wavio
import speech_recognition
import os


def record_audio(file_name, duration):
    fs = 44100

    print("Recording...")
    recording = sounddevice.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sounddevice.wait()
    wavio.write(file_name, recording, fs, sampwidth=2)
    print("Recording complete")


def recognize_speech(file_name):
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(file_name) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            if os.path.exists(file_name):
                os.remove(file_name)
            else:
                print("The file does not exist")
            return text
        except speech_recognition.UnknownValueError:
            print("Sorry, I could not understand the audio")
        except speech_recognition.RequestError as e:
            print(f"Could not request results; {e}")

    return ""
