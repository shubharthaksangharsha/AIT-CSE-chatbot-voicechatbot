import poe
import sys
import logging
from IPython.display import display, Markdown, Latex
poe.logger.setLevel(logging.INFO)
token = 'iCHyh9WWaHuOXzruBStEVQ%3D%3D'

client = poe.Client(token)

def say(msg):
    ans = ''
    for chunk in client.send_message('chinchilla', msg, with_chat_break=False):
#         print(not chunk['text_new'].find("'''"))
#         if not chunk['text_new'].find("'''"):
#             print(chunk['text_new'], end=' ', flush=True)
         ans += chunk['text_new']
        #yield(chunk['text_new'])
         print(chunk['text_new'], end = '', flush=True)
    # return ans
#         
#     res = Markdown(ans + ' ')
#     display(res)
#     print(display(res), end=' ')

if __name__ == '__main__':
     while True:
          msg = input('> ')
          if 'bye' in msg or 'exit' in msg: 
               break
          say(msg)
          print()
     print('Thank you for using me')
# import tkinter as tk

# # create a new Tkinter window
# window = tk.Tk()
# window.title("Chatbot GUI")

# # create a text box to display the chat history
# chat_history = tk.Text(window, height=20, width=50)
# chat_history.pack()

# # create a label and an entry field for user input
# label = tk.Label(window, text="User Input:")
# label.pack()
# user_input = tk.Entry(window)
# user_input.pack()

# # define a function to handle user input
# def send_message():
#     # get user input and clear the entry field
#     message = user_input.get()
#     user_input.delete(0, tk.END)

#     # add user input to the chat history
#     chat_history.insert(tk.END, "You: " + message + "\n")

#     # get response from the chatbot
#     response = say(message)

#     # add chatbot response to the chat history
#     chat_history.insert(tk.END, "Chatbot: " + response + "\n")

# # create a button to send user input
# send_button = tk.Button(window, text="Send", command=send_message)
# send_button.pack()

# # start the Tkinter event loop
# window.mainloop()

