from gtts import gTTS 
import os 
import pyttsx3

def speak(text):
    speech = gTTS(text=text, lang="en-in", slow=False)
    speech.save("text.mp3")
    os.system("mpg123 text.mp3")

def Say(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine. setProperty( "voices" , voices[0].id)
    engine. setProperty("rate" ,170)
    print("  ")
    print(f"A.1 : {text}")
    engine.say(text=text)
    engine.runandWait()
    print("   ")

if __name__ == '__main__':
    pass