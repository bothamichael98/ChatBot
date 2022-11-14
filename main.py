#Michael Botha
#218550819
#DESIGN  PROJECT III (2022/2)

__author__ = "Michael Botha"
__copyright__ = "Copyright 2022, DESIGN  PROJECT III TUT Chatbot system"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Michael Botha"
__email__ = "218550819@tut4life.ac.za"
__status__ = "Final Project"



"""
Python interpreter:
sudo apt-get install python3-tk
python3 -m pip install pillow
pip install chatterbot
"""
#Import's
import tkinter as tk #For GUI using Tkinter
from tkinter import messagebox
import datetime #For generating date and time
from PIL import ImageTk, Image#To add watermark on page
import csv#to open and read CSV files
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import sqlite3
import os
import socket
import base64
import Client

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.8.87', 4141)


#Create BOTs
userBot = ChatBot(
    name='Stock Take Bot',
    read_only=True,
    logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.TimeLogicAdapter']
)
# Train the BOT
ChatBot_trainee = ChatterBotCorpusTrainer(userBot)
ChatBot_trainee.train("chatterbot.corpus.english.greetings")
ChatBot_trainee.train("chatterbot.corpus.english.conversations")
ChatBot_trainee.train("chatterbot.corpus.english.botprofile")                     
ChatBot_trainee.train("chatterbot.corpus.english.ID")
ChatBot_trainee.train("chatterbot.corpus.english.PRICE")

guestBot = ChatBot(
    name='Stock Take Bot',
    read_only=True,
    logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.TimeLogicAdapter']
)
# Train the BOT
ChatBot_trainee = ChatterBotCorpusTrainer(guestBot)
ChatBot_trainee.train("chatterbot.corpus.english.greetings")
ChatBot_trainee.train("chatterbot.corpus.english.ID")
ChatBot_trainee.train("chatterbot.corpus.english.conversations")
ChatBot_trainee.train("chatterbot.corpus.english.botprofile")   


#Creat Login Window
loginWindow =tk. Tk()
loginWindow.title("Chatbot")
loginWindow.geometry("800x450+10+10")
loginWindow.resizable(False,False)
#loginWindow.iconbitmap(r'Icon.ico')

#Generate logo
img = ImageTk.PhotoImage(Image.open("tut.png"))
imgLabel = tk.Label(loginWindow,image=img)
imgLabel.place(x=480,y=110)

#Generate live timestamp
def date_time():
    now =datetime.datetime.now()
    dateTime = now.strftime("%Y-%m-%d %H:%M:%S %p")
    timeLabel.config(text=dateTime)
    timeLabel.after(200, date_time)
timeLabel = tk.Label(loginWindow, font=('Arial', 10, 'bold'), fg="black", bd =30)
timeLabel.grid(row =0, column=0)
timeLabel.place(relx=0.73,relheight=0.05)

#Generate welkom Message
welkomLabel = tk.Label(loginWindow, text="Welkom to the automated chatbot service desk\n"
                                         "Please login" ,font=('Arial', 14,'bold'))
welkomLabel.place(relx=0.25,rely=0.2)

#Generate Login fields
username = tk.Label(loginWindow, text="Username" ,font=('Arial', 14))
password = tk.Label(loginWindow, text="Password" ,font=('Arial', 14))
userEnter = tk.Entry(loginWindow, show=None, font=('Arial', 24))
passEnter = tk.Entry(loginWindow, show='*', font=('Arial', 24))
userEnter.place(x=225,y=180)
passEnter.place(x=225,y=250)
username.place(x=215,y=150)
password.place(x=215,y=225)

fileName = "log.txt"


#Login Process
def login():
    login_User = userEnter.get()
    login_Pass = passEnter.get()+''
    with open(r'userFile.csv') as userFile:
        csv_file_reader = csv.reader(userFile, delimiter=',')

        for row in csv_file_reader:
            if login_User == row[0]:#Check username
                user_pass_enc = base64.b64encode(login_Pass.encode())
                print(user_pass_enc.decode())
                if user_pass_enc.decode() == row[1]:#Check password
                    
                    #Generate YML
                    def write_DB():
                        conn = sqlite3.connect('/home/pi/Documents/TEMP/PTA_local_stock.db')
                        cursor = conn.execute("SELECT ID,NAME,COLOUR,QTY,PRICE from STOCK")
                        tmp_file_ID="catagory:\n- Stock\nconversations:\n"
                        tmp_file_Price="catagory:\n- Stock\nconversations:\n"
                        for row in cursor:
                           tmp_file_ID=tmp_file_ID+"- - Do you have a "+row[1]+"\n"+"  - Yes, We have " + str(row[3])+" "+row[1]+"s in stock\n"
                           tmp_file_ID = tmp_file_ID + "- - What colour is the " + row[1] + "\n" + "  - The colour is " +row[2] + "\n"
                           tmp_file_ID = tmp_file_ID + "- - What is the price of a " + row[1] + "\n" + "  - The price is R" +str(row[4]) + "0 each\n"
                        with open(r'/home/pi/Documents/TUTChatbot/TEMP_ID.txt','w')as file:
                           file.write(tmp_file_ID)
                        os.remove(r'/home/pi/.local/lib/python3.9/site-packages/chatterbot_corpus/data/english/ID.yml')
                        os.rename(r'/home/pi/Documents/TUTChatbot/TEMP_ID.txt',r'/home/pi/.local/lib/python3.9/site-packages/chatterbot_corpus/data/english/ID.yml')
                        conn.close()
                        userBot.storage.drop()
                        ChatBot_trainee.train("chatterbot.corpus.english.greetings")
                        ChatBot_trainee.train("chatterbot.corpus.english.ID")
                        ChatBot_trainee.train("chatterbot.corpus.english.conversations")
                        ChatBot_trainee.train("chatterbot.corpus.english.botprofile") 
                        
                    write_DB()
                    nowLI = datetime.datetime.now()
                    dateTimeLI = nowLI.strftime("%Y-%m-%d %H:%M:%S %p")
                    with open("log.txt", 'a') as userF:# To Log user login
                        userF.write(''.join(row[2]+" "+row[3]+" has logged in at "+dateTimeLI+"\n"))
                    userEnter.delete(0, 100)##Delete username after login
                    passEnter.delete(0, 100)#Delete password after login
                    #CODE HERE
                    UserWindow = tk.Tk()
                    UserWindow.title("Chatbot")
                    UserWindow.geometry("800x450+10+10")
                    UserWindow.resizable(False, False)  # lock resizable
                    #UserWindow.iconbitmap(r'Icon.ico')

                    # Welkom Label
                    usersName = row[2]+" "+row[3]
                    welkomLb = tk.Label(UserWindow, text="Welkom "+usersName+
                                                            " to the automated chatbot service desk",
                                                            font=('Arial', 14, 'bold'))
                    welkomLb.place(relx=0.2, rely=0.2)


                    def gen_Respons():
                        response = userBot.get_response(question.get())
                        question.delete(0,100)
                        prntResponse = str(response) + "\n" + "Do you want to ask another qeustion?"
                        result = messagebox.askquestion("Result", prntResponse,parent=UserWindow)
                        with open("log.txt", 'a') as userF:
                            userF.write(''.join("***\n-Question: " + str(question.get()) + "\n" + "-Answer: " + str(response) + "\n*** \n"))
                        if result == 'yes':
                            UserWindow.lift()
                        else:
                            UserWindow.destroy()

                    def udp_client():

                        Client.udp_client(usersName)

                    userAskLB = tk.Label(UserWindow, text="Not getting the answer you are looking for?",
                                         font=('Arial', 14, 'bold'))
                    userAskLB.place(x=100,y=320)
                    userAsk_button = tk.Button(UserWindow, text='Ask a user', bg='#Ff0000', fg='#ffffff',
                                               command=udp_client)
                    userAsk_button['font'] = ('Arial', 14)
                    userAsk_button.place(x=100,y=350)

                    # exit button
                    def destroy_window():

                        result = messagebox.askquestion("Exit", "Do you want to Exit?",parent=UserWindow)
                        if result == 'yes':
                            nowLO = datetime.datetime.now()
                            dateTimeLO = nowLO.strftime("%Y-%m-%d %H:%M:%S %p")
                            with open("log.txt", 'a') as userF:
                                userF.write(''.join(row[2] + " " + row[3] + " has logged out at " + dateTimeLO + "\n"))
                            UserWindow.destroy()
                            #userBot.storage.drop()
                        else:
                            UserWindow.lift()

                    # exit button
                    exit_button = tk.Button(UserWindow, text='Exit', bg='#Ff0000', fg='#ffffff',
                                            command=destroy_window)


                    def date_time():
                        now = datetime.datetime.now()
                        dateTime = now.strftime("%Y-%m-%d %H:%M:%S %p")
                        timeLabel.config(text=dateTime)
                        timeLabel.after(200, date_time)

                    timeLabel = tk.Label(UserWindow, font=('Arial', 10, 'bold'), fg="black", bd=30)
                    timeLabel.grid(row=0, column=0)
                    timeLabel.place(relx=0.73, relheight=0.05)
                    date_time()

                    nowLI = datetime.datetime.now()
                    dateTimeLI = nowLI.strftime("%Y-%m-%d %H:%M:%S %p")
                    with open('log.txt', 'a') as userF:# To Log user login
                        userF.write(''.join(row[2]+" "+row[3]+" has logged in at "+dateTimeLI+"\n"))

                    question = tk.Entry(UserWindow, show=None, font=('Arial', 24), width=50)
                    question.place(x=50, y=100)
                    question.pack(side=tk.LEFT, padx=10)


                    ask_button = tk.Button(UserWindow, text="Ask", height="2", width="20", command=gen_Respons)
                    ask_button.place(relx=0.4, y=250)

                    exit_button['font'] = ('Arial', 14)
                    exit_button.pack(ipadx=10, ipady=10)
                    exit_button.place(x=700, y=400)


                    UserWindow.mainloop()
                else:
                    errorLogin = messagebox.showwarning("Error","Password Incorrect\n"
                                                                "Please try again",parent=UserWindow)
            else:
                errorLogin = messagebox.showwarning("Error", "Username not found"
                                                             "Please try again",parent=UserWindow)
def guestLogin():
    guestWindow = tk.Tk()
    guestWindow.title("Chatbot")
    guestWindow.geometry("800x450+10+10")
    guestWindow.resizable(False, False)# lock resizable
    #guestWindow.iconbitmap(r'Icon.ico')

    #Welkom Label
    welkomLb = tk.Label(guestWindow, text="Welkom guest user to the automated chatbot service desk",font=('Arial', 14,'bold'))
    welkomLb.place(relx=0.2, rely=0.2)



    def udp_client():

        Client.udp_client('Guest user')
        
    userAskLB = tk.Label(guestWindow, text="Not getting the anser you are looking for?",font=('Arial', 14,'bold'))
    userAskLB.place(x=100,y=320)
    userAsk_button = tk.Button(guestWindow, text='Ask a user', bg='#Ff0000', fg='#ffffff', command=udp_client)
    userAsk_button['font'] = ('Arial', 14)
    userAsk_button.place(x=100,y=350)

    def destroy_window():

        result = messagebox.askquestion("Exit", "Do you want to Exit?", parent=guestWindow)
        if result == 'yes':
            nowLO = datetime.datetime.now()
            dateTimeLO = nowLO.strftime("%Y-%m-%d %H:%M:%S %p")
            with open("log.txt", 'a') as userF:
                userF.write(''.join("Guest User has logged out at " + dateTimeLO + "\n"))
            guestWindow.destroy()

        else:
            guestWindow.lift()
    #exit button
    exit_button = tk.Button(guestWindow,text='Exit',bg='#Ff0000',fg='#ffffff',command= destroy_window)
    exit_button['font'] = ('Arial', 14)
    exit_button.pack(ipadx=10, ipady=10)
    exit_button.place(x=700, y=400)

    #Generate YML
    def write_DB():
        conn = sqlite3.connect('/home/pi/Documents/TEMP/PTA_local_stock.db')
        cursor = conn.execute("SELECT ID,NAME,COLOUR,QTY,PRICE from STOCK")
        tmp_file_ID="catagory:\n- Stock\nconversations:\n"
        tmp_file_Price="catagory:\n- Stock\nconversations:\n"
        for row in cursor:
            tmp_file_ID=tmp_file_ID+"- - Do you have a "+row[1]+"\n"+"  - Yes, We have " + str(row[3])+" "+row[1]+"s in stock\n"
            tmp_file_ID = tmp_file_ID + "- - What colour is the " + row[1] + "\n" + "  - The colour is " +row[2] + "\n"
            tmp_file_ID = tmp_file_ID + "- - What is the price of a " + row[1] + "\n" + "  - The price is R" +str(row[4]) + "0 each\n"
        with open(r'/home/pi/Documents/TUTChatbot/TEMP_ID.txt','w')as file:
            file.write(tmp_file_ID)
        os.remove(r'/home/pi/.local/lib/python3.9/site-packages/chatterbot_corpus/data/english/ID.yml')
        os.rename(r'/home/pi/Documents/TUTChatbot/TEMP_ID.txt',r'/home/pi/.local/lib/python3.9/site-packages/chatterbot_corpus/data/english/ID.yml')
        conn.close()
        guestBot.storage.drop()
        ChatBot_trainee.train("chatterbot.corpus.english.greetings")
        ChatBot_trainee.train("chatterbot.corpus.english.ID")
        ChatBot_trainee.train("chatterbot.corpus.english.conversations")
        ChatBot_trainee.train("chatterbot.corpus.english.botprofile") 
                    
    write_DB()
    def date_time():
        now = datetime.datetime.now()
        dateTime = now.strftime("%Y-%m-%d %H:%M:%S %p")
        timeLabel.config(text=dateTime)
        timeLabel.after(200, date_time)
    timeLabel = tk.Label(guestWindow, font=('Arial', 10, 'bold'), fg="black", bd=30)
    timeLabel.grid(row=0, column=0)
    timeLabel.place(relx=0.73, relheight=0.05)
    date_time()

    nowLI = datetime.datetime.now()
    dateTimeLI = nowLI.strftime("%Y-%m-%d %H:%M:%S %p")
    with open('log.txt', 'a') as userF:  # To Log user login
        userF.write(''.join("A Guest user has logged in at " + dateTimeLI + "\n"))

    question_g = tk.Entry(guestWindow,show=None, font=('Arial', 24),width=40)
    question_g.place(x=50,y=100)
    question_g.pack(side=tk.LEFT,padx=10)




    def gen_Respons_g():
        response = guestBot.get_response(question_g.get())

        tmp_word = question_g.get()
        if tmp_word.find('price') !=-1:
            question_g.delete(0, 100)
            tempResponse="Guests can't ask that question"
            prntResponse = tempResponse+"\nDo you want to ask another question"
            with open("log.txt", 'a') as userF:
                userF.write(''.join("***\n-Question: " + tmp_word + "\n" + "-Answer: " + tempResponse+"\n*** \n"))
        else:
            question_g.delete(0, 100)
            prntResponse = str(response) + "\n"+"Do you want to ask another question?"
            with open("log.txt", 'a') as userF:
                userF.write(''.join("***\n-Question: " + tmp_word + "\n" + "-Answer: " + str(response)+"\n*** \n"))

        result = messagebox.askquestion("Result", prntResponse,parent=guestWindow)
        
        if result == 'yes':
            guestWindow.lift()
        else:
            nowLO = datetime.datetime.now()
            dateTimeLO = nowLO.strftime("%Y-%m-%d %H:%M:%S %p")
            with open('log.txt', 'a') as userF:  # To Log user login
                userF.write(''.join("A Guest user has logged out at " + dateTimeLO + "\n"))
            guestWindow.destroy()



    ask_button = tk.Button(guestWindow, text="Ask", height="2", width="20", command=gen_Respons_g)
    ask_button.place(relx=0.4, y=250)





    guestWindow.mainloop()


submit_button=tk.Button(loginWindow,text="Login", height="2", width="30",command=login)
submit_button.place(x=225,y=300)
guest_button=tk.Button(loginWindow,text="Guest Login", height="2", width="30",command=guestLogin)
guest_button.place(x=225,y=350)

#userBot.storage.drop()
#guestBot.storage.drop()
date_time()#Loop date and time
loginWindow.mainloop()  # Loop the main Login window








