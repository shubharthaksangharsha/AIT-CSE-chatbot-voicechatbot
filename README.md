# AI Chatbot

The AI Chatbot is a project that utilizes Natural Language Processing (NLP) techniques to create a conversational chatbot. It enables voice command recognition, tokenization, stemming, and bag of words representation for text processing.

**Requirements**
Python 3.6 or above
NumPy library (install using pip install numpy)
NLTK library (install using pip install nltk)
Setup
Clone the repository:

```
git clone https://github.com/shubharthaksangharsha/AIT-CSE-chatbot-voicechatbot.git
```
Install the required dependencies:
```
pip install -r requirement.txt
```
Run the main script:
```
python main.py

```

### Usage
Voice Command Recognition:

The takeCommand() function in the speech_recognition.py file enables voice command recognition from the user's microphone input.
It listens to the user's voice, converts it into text, and returns the recognized speech.
NLP Techniques:

Tokenization:

The tokenize() function in the nlp_utils.py file tokenizes a given sentence using the NLTK library.
It splits the sentence into a list of individual words.
Stemming:

The stem() function in the nlp_utils.py file performs word stemming using the PorterStemmer algorithm from the NLTK library.
It reduces words to their root or base form.
Bag of Words:

The bag_of_words() function in the nlp_utils.py file creates a bag of words representation for a given tokenized sentence.
It generates a binary vector where each element represents the presence or absence of a word from a predefined list of words in the sentence.

# AI Chatbot

The AI Chatbot is a project that utilizes Natural Language Processing (NLP) techniques to create a conversational chatbot. It enables voice command recognition, tokenization, stemming, and bag of words representation for text processing.

**Requirements**
Python 3.6 or above
NumPy library (install using pip install numpy)
NLTK library (install using pip install nltk)
torch library (install using pip install torch)
SpeechRecognition library (install using pip install SpeechRecognition)
gtts library (install using pip install gtts)
pytz library (install using pip install pytz)
schedule library (install using pip install schedule)
pyaudio library (install using pip install pyaudio)
pvporcupine library (install using pip install pvporcupine)
pandas library (install using pip install pandas)

Setup
Clone the repository:

```
git clone https://github.com/shubharthaksangharsha/AIT-CSE-chatbot-voicechatbot.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Run the main script:
```
python main.py

```

**Features**

**AIT-CSE Chatbot**: This option allows the user to interact with the AIT-CSE Chatbot. It most likely involves text-based conversations where the chatbot responds to user queries and performs specific tasks related to AIT-CSE.

**AIT-CSE VoiceChatbot**: This option provides a voice-based interaction with the AIT-CSE Chatbot. It enables users to speak their queries or commands instead of typing them. The chatbot uses speech recognition and synthesis to understand and respond to user input.

**ChatGPT for External Queries**: This option utilizes ChatGPT, an external chatbot model, to handle queries beyond the capabilities of the AIT-CSE Chatbot. ChatGPT is a language model designed to generate human-like responses and can provide more general information or engage in casual conversations.


#### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
