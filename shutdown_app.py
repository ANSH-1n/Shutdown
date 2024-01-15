from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")    


shutdown =Tk()
shutdown.title("Shutdown")
shutdown.geometry('500x500')
shutdown.config(bg="blue")

r_button = Button(shutdown,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor='plus',command=restart())
r_button.place(x=150,y=60,height=50,width=200)

restart_button = Button(shutdown,text="Restart time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor='plus',command=restart_time())
restart_button.place(x=150,y=170,height=50,width=200)

log_out = Button(shutdown,text="Log-Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor='plus',command=logout())
log_out.place(x=150,y=270,height=50,width=200)

shutdown = Button(shutdown,text="Shutdown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor='plus',command=shutdown())
shutdown.place(x=150,y=370,height=50,width=200)


shutdown.mainloop()
