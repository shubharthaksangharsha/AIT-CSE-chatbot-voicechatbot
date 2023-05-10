import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import readline
from gtts import gTTS
import traceback
import speech_recognition as sr
import psutil as ps
import os
import json
import random
import pytz
import schedule
import datetime
import pyaudio
import struct
from ast import keyword
import random
from email.message import EmailMessage
import pvporcupine
import pandas as pd
from datetime import date
import numpy as np 
import sys
pico_key= os.getenv("pico_key")
say = ['say/1.mp3', 'say/2.mp3', 'say/3.mp3', 'say/4.mp3']


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json','r') as json_data:
    intents = json.load(json_data)

FILE = 'TrainData.pth'
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-------------------------
Name = "Apsara"

from Listen import takeCommand, takeCommand5
from Speak import speak
from Tasks import NonInputExecution, InputExecution
def main():
    # sentence = takeCommand().lower()
    sentence = takeCommand().lower()

    if sentence == 'bye' or sentence == 'exit':
        speak('Thank you for using me Sir')
        exit()
    
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim = 1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                if tag == 'bye':
                    speak('Goodbye sir')
                    exit()
                reply = random.choice(intent['responses'])            
                if "time" in reply:
                    ans = NonInputExecution(reply)
                    print(ans)
                    speak(ans)
                elif "date" in reply:
                    ans = NonInputExecution(reply)
                    print(ans)
                    speak(ans)
                elif "day" in reply:
                    ans = NonInputExecution(reply)
                    print(ans)
                    speak(ans)
                elif "wikipedia" in reply:
                    ans = InputExecution(reply, sentence)
                    print(ans)
                    speak(ans)
                elif "search" in reply:
                    ans = InputExecution(reply, sentence)
                    print(ans)
                    speak(f'Here the details of {ans[1]} ')
                    print(ans)

                elif 'class' in reply:
                    ans = InputExecution(reply, sentence)
                    print(ans)
                    speak(ans)
                else:
                    print(reply)
                    speak(reply)
    else:
        print("I'm sorry, I don't have the answer to that question")
        speak("I'm sorry, I don't have the answer to that question")
if __name__ == '__main__':
    porcupine = None
    audio_stream = None
    paudio = None
    battery_flag = 0
    try: 
        porcupine = pvporcupine.create(access_key = pico_key, keyword_paths=['./apsara_keyword/ap-sara_en_linux_v2_1_0.ppn','./apsara_keyword/app-sara_en_linux_v2_1_0.ppn', 'apsara_keyword/hey_jarvis.ppn'])
        paudio = pyaudio.PyAudio()
        audio_stream = paudio.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)
        while True:
            try:
                keyword = audio_stream.read(porcupine.frame_length)
                keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
                keyword_index = porcupine.process(keyword)
                schedule.run_pending()
                if (not ps.sensors_battery().power_plugged and int(ps.sensors_battery().percent) < 10):
                    speak('Sir Please charge me')
                    battery_flag = 1
                
                if ps.sensors_battery().power_plugged and battery_flag:
                    speak('Thank you sir')
                    battery_flag = 0
                    
                if keyword_index >= 0:
                    # check = subprocess.Popen('pacmd list-sink-inputs | grep -w state', shell=True, stdout=subprocess.PIPE, encoding='UTF-8').stdout.readline().split()
                    # print(check)
                    # if check.count('RUNNING') >= 1:
                    print("Called Apsara!")
                    os.system(f'mpg123 {random.choice(say)}')
                    # os.system(f'aplay output4.wav')
                    try:
                        main()
                        # query = takeCommand5().lower()
                    except:
                        print("exception occured!!")
                        pass
            except Exception:
                print(traceback.format_exc())
                print('Unable to understand')
            else:     
                pass
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paudio is not None:
            paudio.terminate()
