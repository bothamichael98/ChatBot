import socket
import tkinter as tk
import datetime
from tkinter import messagebox

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.8.87', 4141)
print("Connected")

def udp_client(user_name):

    # Send data
    try:

        CommWindowC = tk.Tk()
        CommWindowC.title("Client")
        CommWindowC.geometry("800x450+10+10")
        CommWindowC.resizable(False, False)

        tLabel = tk.Label(CommWindowC, font=('Arial', 10, 'bold'), fg="black", bd=30)
        tLabel.grid(row=0, column=0)
        tLabel.place(relx=0.73, relheight=0.05)

        def date_time():
            now = datetime.datetime.now()
            dateTime = now.strftime("%Y-%m-%d %H:%M:%S %p")
            tLabel.config(text=dateTime)
            tLabel.after(200, date_time)

        date_time()


        responsLbl = tk.Label(CommWindowC, text="Enter your response here:", font=('Arial', 14))
        responsEnt = tk.Entry(CommWindowC, show=None, font=('Arial', 24))
        responsEnt.place(x=115,
                         y=150,
                         width=600,
                         height=50)
        responsLbl.place(x=125, y=110)

        def send_Respons():
            responsStr = user_name + " asks a question:\n"+responsEnt.get()
            sent = sock.sendto(responsStr.encode("utf-8"), server_address)
            CommWindowC.quit()

        submit_button = tk.Button(CommWindowC, text="Send", height="2", width="20", command=send_Respons)
        submit_button.place(x=125, y=250)
        submit_button['font'] = ('Arial', 14)

        cancel_button = tk.Button(CommWindowC, text="Exit", height="2", width="20",fg="red", command=CommWindowC.destroy)
        cancel_button.place(x=125, y=320)
        cancel_button['font'] = ('Arial', 14)

        CommWindowC.mainloop()


        # Receive response
        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        print(data.decode("utf-8"))
        messageRC = data.decode("utf-8")
        with open("log.txt", 'a') as userF:
            userF.write(''.join("***\n-Question: " + responsStr + "\n" + "-Answer: " + messageRC+"\n*** \n"))
        input_boxC=tk.messagebox.askquestion(title='Incoming Answer', message=messageRC + "\nDo you want to ask again?",parent=CommWindowC)

        if input_boxC == 'yes':
            print ("Yes")
            CommWindowC.destroy()
            udp_client(user_name)
        else:
            print('closing socket')
            sock.close()


    finally:
        print('closing socket')
        #sock.close()



#udp_client()

