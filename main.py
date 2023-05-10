import os 
import sys 

if __name__ == '__main__':
    print('Welcome to AIT-CSE Chatbot and VoiceChatbot')
    print("1. Use AIT-CSE Chatbot")
    print("2. Use AIT-CSE VoiceChatbot")
    print("3. Use ChatGPT for external queries")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        os.system('python3 Apsara_Chatbot.py')
    elif choice == 2:
        os.system('python3 Apsara_VoiceChatbot.py')
    elif choice == 3:
        os.system('python3 ChatGPT.py')
    elif choice == 4:
        print("Thank you for using me")
        exit()
    else:
        print("Invalid choice")
        exit()

