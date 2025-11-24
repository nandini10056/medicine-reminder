import time
from datetime import datetime,timedelta
import winsound
medicine_list=[]
total=int(input("Input total number of prescribed medicines "))
for i in range(total):
    meds=input("Enter medicine name: ")
    reminder=float(input("Time(in hours) after which you should take medicine "))
    medicine_list.append((meds,reminder))
while True:
    for meds,reminder in medicine_list:
        present=datetime.now()
        remindertime=present+timedelta(hours=reminder)
        print("Current time:",present.strftime("%H:%M:%S"))
        print("Take medicine at",remindertime.strftime("%H:%M:%S"))
        reminder_sec=reminder*60*60
        time.sleep(reminder_sec)
        winsound.Beep(1000,1000)
        print("Reminder- Take medicine: ",meds)
    next=input("Have you finished the prescribed dose?(yes/no)")
    if next.lower()=="yes":
        print("Terminating further reminders")
        break
