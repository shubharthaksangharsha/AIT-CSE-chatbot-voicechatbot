import datetime
import wikipedia
import pandas as pd 
record = pd.read_csv('records.csv')
record.set_index('uid', inplace=True)
import pandas as pd
import datetime

def today_class():  
    # Create a list of tuples for the data
    data = [
        ("9:30-10:20", "TOC", "NLP Theory", "AI Theory", "Aptitude", "AI Lab"),
        ("10:20-11:00", "NLP Lab", "TOC", "NOS Theory", "Aptitude", "AI Lab"),
        ("11:10-12:00", "NLP Lab", "NOS Theory", "NLP Theory", "No class", "No class"),
        ("13:00-13:50", "AI Theory", "No class", "NOS Lab", "NOS Theory", "Technical Training Lab"),
        ("13:50-14:40", "No class", "Soft Skill", "Nos Lab", "NLP Theory", "Technical Training Lab"),
        ("14:40-15:30", "No class", "Soft Skill", "No class", "TOC Theory", "No class"),
        ("15:30-15:20", "Minor Project", "No class", "No class", "No class", "AI Theory")]

    # Create the pandas dataframe
    df = pd.DataFrame(data, columns=["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

    # Set the "Time" column as the index
    df.set_index("Time", inplace=True)

    # Set the column names to lowercase for ease of use
    df.columns = df.columns.str.lower()
    print(df)
    # Set the index to the days of the week
    df.index.name = "Day"

    # Determine the current time and day of the week
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    current_day = now.strftime("%A")
    print("TIME", end='')
    print(current_day)
    print(current_time)
    # Find the nearest time slot based on the current time
    time_slots = list(df.index)
    time_slots.append(current_time)
    # time_slots.append('13:00')
    time_slots.sort()
    print(time_slots)
    current_time_index = time_slots.index(current_time)
    # current_time_index = time_slots.index('13:00')
    current_time_index = time_slots.index()

    # Find the subject for the current time and day of the week
    # print(current_time, current_time_index, current_day)
    current_subject = df.iloc[current_time_index - 1, df.columns.get_loc(current_day.lower())]

    # Reply with the subject for the current time and day of the week
    if pd.isna(current_subject):
        print("There is no class at the current time.")
    else:
        print(f"Your current class or next class is of {current_subject}.")

def get_student_details(id):
    id = id.upper() 
    if isinstance(id, str):
        # If UID is provided
        return record.loc[id],record.loc[id][0]


def Time():
    time = datetime.datetime.now().strftime('%H:%M')
    return time

def Date():
    date = datetime.datetime.today()
    return date 

def Day():
    day = datetime.datetime.now().strftime("%A")
    return day

    
def NonInputExecution(query):
    query = str(query)
    if 'time' in query:
        print(Time())

    if 'date' in query:
        print(Date())

    if 'day' in query:
        print(Day())

    if 'class' in query:
        today_class()



#2 - Input
#eg - google search, wikipedia 

def Wikipedia(tag, query):
    name = str(query).replace("who is", "").replace("about", "").replace("what is", "").replace("wikipedia", "")
    result = wikipedia.summary(name)
    print(result)    

def Search(tag, query):
    UID = input("Enter the UID of the student: ")
    print(get_student_details(UID))

def InputExecution(tag, query):

    if "wikipedia" in tag:
        Wikipedia(tag, query)

    if "search" in tag:
        print(tag, query)
        Search(tag, query)