import datetime
import time
from tkinter import *

from pygame import mixer

root = Tk() #Window Initialization
root.title('MyAlarm Clock') #Title of the window
root.config(bg='lightgreen') #Setting the Background Color
root.geometry('550x400') #Setting the default size of the Window
root.iconbitmap('favicon.ico') # Favicon 

hrs = StringVar() #To Store Value of Hour
mins = StringVar() #To Store Value of Minutes

#To convert the values into a proper Timestamp
def set_alarm():
    alarmtime = f'{hrs.get()}:{mins.get()}:00'
    if alarmtime != ': :00':
        alarmclock(alarmtime)

# Main Function to run the clock
def alarmclock(alarm_time):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime('%H:%M:%S') #Current Time
        print(time_now)
        if time_now == alarm_time:
            Label(root, text='Wake UP!Wake UP!Wake UP!', bg='lightgreen', font=('arial', 20, 'italic')).grid(padx=20,
                                                                                                             pady=10,
                                                                                                             row=2,
                                                                                                             column=2)
            print('Wake Up!')
            mixer.init()
            mixer.music.load('alarm.mp3')
            mixer.music.play(loops=3)
            break


Label(root, text='Take a Short Nap!Enter the time in 24 HOURS Format', font=('arial', 20, 'italic'), bg='lightgreen').grid(row=1, column=2)
Label(root, text='Hours:', font=('arial', 20, 'italic'), bg='lightgreen').grid(sticky='e', row=3, column=1)
Label(root, text='Minutes:', font=('arial', 20, 'italic'), bg='lightgreen').grid(sticky='e', row=4, column=1)

hrs_entry = Entry(root, textvariable=hrs, width=5, font=('arial', 20, 'italic'))
hrs_entry.grid(padx=1, pady=10, row=3, column=2)
min_entry = Entry(root, textvariable=mins, width=5, font=('arial', 20, 'bold'))
min_entry.grid(padx=1, pady=10, row=4, column=2)

set_btn = Button(root, command=set_alarm, text='Set Alarm', bg='lightgreen', fg='black',
                 font=('arial', 20, 'italic')).grid(padx=40, pady=30, row=7, column=2)
mainloop() #Execution of the Window
# Enjoy Your Personal Self Built Alarm Clock😎😎
