
from tkinter import *
import os

clock = Tk()                                        # Calling the class
clock.title('Digital Clock')
clock.geometry("470x206")
clock.config(bg = "Red")              # Configure Background colour
lab_hr = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='blue', fg='yellow')
lab_hr.place(x=20, y=20, height=50, width=50)

lab_hr_txt = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='red', fg='yellow')
lab_hr_txt.place(x=20, y=70, height=30, width=50)

lab_min = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='blue', fg='yellow')
lab_min.place(x=90, y=20, height=50, width=50)

lab_min_txt = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='red', fg='yellow')
lab_min_txt.place(x=90, y=70, height=30, width=50)

lab_sec = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='blue', fg='yellow')
lab_sec.place(x=160, y=20, height=50, width=50)

lab_sec_txt = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='red', fg='yellow')
lab_sec_txt.place(x=160, y=70, height=30, width=50)

lab_am = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='blue', fg='yellow')
lab_am.place(x=230, y=20, height=50, width=50)

lab_am_txt = Label(clock, text="00", font=('Time New Roman', 20, "bold"),
               bg='red', fg='yellow')
lab_am_txt.place(x=230, y=70, height=30, width=50)


#__________________________________________________________________________________________

def Restart():
    os.system("shutdown /r /t 1")

def Restart_Time():
    os.system("shutdown /r /t 20")

def LogOut():
    os.system("shutdown -l")

def Shutdown():
    os.system("shutdown /s /t 1")

r_button = Button(clock, text = "Restart", font = ("Time New Roman", 15, "bold"),
                  relief = RAISED, cursor = "plus", command=Restart)
r_button.place(x=300, y=20, height=34, width=150)

rt_button = Button(clock, text = "Timed Restart", font = ("Time New Roman", 15, "bold"),
                  relief = RAISED, cursor = "plus", command=Restart_Time)
rt_button.place(x=300, y=64, height=34, width=150)

lg_button = Button(clock, text = "Log Out", font = ("Time New Roman", 15, "bold"),
                  relief = RAISED, cursor = "plus", command=LogOut)
lg_button.place(x=300, y=108, height=34, width=150)

sd_button = Button(clock, text = "Shutdown", font = ("Time New Roman", 15, "bold"),
                  relief = RAISED, cursor = "plus", command=Shutdown)
sd_button.place(x=300, y=152, height=34, width=150)


clock.mainloop()                                    # Running forever


