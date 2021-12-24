#PORTSCANNER
#Filip Rokita
#www.filiprokita.com

#import
import tkinter as tk
import socket
from tkinter import messagebox

#def
def check():
    ip = ipVar.get()
    port = int(portVar.get())
    location = (ip, port)

    sock = socket.socket()
    result = sock.connect_ex(location)
    if result == 0:
        messagebox.showinfo(title='PORTSCANNER', message=f'IP: {ip}\nPort: {port}\n\nOPEN')
    else:
        messagebox.showinfo(title='PORTSCANNER', message=f'IP: {ip}\nPort: {port}\n\nCLOSED')





#main
if __name__ == '__main__':
    root = tk.Tk()
    root.title('PORTSCANNER')
    root.geometry('300x150')
    root.resizable(False, False)

    ipVar = tk.StringVar()
    portVar = tk.StringVar()

    ipL = tk.Label(root, text='IP'); ipL.pack()
    ipE = tk.Entry(root, textvariable=ipVar); ipE.pack()
    portL = tk.Label(root, text='PORT'); portL.pack()
    portE = tk.Entry(root, textvariable=portVar); portE.pack()
    checkB = tk.Button(root, text='CHECK', command=check); checkB.pack(pady=10)
    authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()

    root.mainloop()