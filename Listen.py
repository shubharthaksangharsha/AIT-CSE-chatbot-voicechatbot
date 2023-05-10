import speech_recognition as sr
#take voice command from the user microphone and convert it into text 
def takeCommand(pause_threshold = 0.6, timeout=5, phrase_time_limit=3):
    """
    This function listens to the user's voice input through the microphone and returns a string output.

    Args:
    pause_threshold (float): The minimum length of silence (in seconds) that is considered the end of a phrase.
    timeout (int): The maximum number of seconds that the function will wait for speech before timing out and returning.
    phrase_time_limit (int): The maximum number of seconds that this function will allow a phrase to continue before stopping and returning the first part of the speech recognized.

    Returns:
    str: The text of the speech recognized from the user's input.

    Raises:
    None
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = pause_threshold
        try:
            audio = r.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
    return query

def takeCommand5():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('takeCommand5')
            print("Listening...")
            r.pause_threshold = 0.6
            audio = r.listen(source,phrase_time_limit = 5,timeout = 3)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
    except Exception as e:
            print("Say that again please")
            print(e)
            return ""
    return query


if __name__ == '__main__':
    pass