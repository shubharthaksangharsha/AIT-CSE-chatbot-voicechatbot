# AI Chatbot

The AI Chatbot is a project that utilizes Natural Language Processing (NLP) techniques to create a conversational chatbot. It enables voice command recognition, tokenization, stemming, and bag of words representation for text processing.

**Requirements**
Python 3.6 or above
NumPy library (install using pip install numpy)
NLTK library (install using pip install nltk)
Setup
Clone the repository:

```
git clone https://github.com/your-username/ai-chatbot.git
```
Install the required dependencies:
```
pip install -r requirements.txt
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


#### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
