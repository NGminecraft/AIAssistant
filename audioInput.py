def main():
    import speech_recognition as sr
    import pyaudio
    import pyttsx3

    r = sr.Recognizer()
    speachToText(r, sr)


def speachToText(r, sr):
    while (0 == 0):

        with sr.Microphone() as source2:
            r.adjust_to_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            text = r.recognize_google(audio2)
            print(text)
