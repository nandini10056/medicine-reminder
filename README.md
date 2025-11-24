
# Smart Medicine Reminder System

A simple and effective Python-based program that reminds users to take their prescribed medicines at the correct time intervals. The program allows users to enter multiple medicines, set reminder intervals, and receive alerts using sound notifications.

## Features

* Add multiple medicines with individual reminder intervals

* Automatically calculates the next reminder time

* Displays current time and reminder time

* Plays a beep sound when it’s time to take the medicine

* Asks the user if the dose is completed

* Stops reminders upon user confirmation

## Technologies Used

* Python 3

* Libraries:
   * time – pauses execution until next reminder
   * winsound(works with windows)-generates audio alert when it's time to take medicine
   * datetime - for handling time calculations
   * timedelta-helps add time intervals for reminders

## How to Run
 1. Run:python medicine_reminder.py

 2. Follow the prompts:
    Enter medicine names
    Enter reminder times
    Wait for alerts


## How It Works

1. The user inputs the total number of medicines.

2. For each medicine:
   * Enter the name
   * Enter the time interval (in hours) after which the reminder should repeat

3. The script continuously checks for reminders inside an infinite loop.

4. When it’s time:
   * Shows the reminder message
   * Plays a notification beep
   * Asks if the user has completed the dose

5. If the user enters “yes”, the program terminates further reminders.

## Real-Life Use
* Helps patients taking regular medicine
* Useful for school/college students
* Helpful for elderly people

## Output Screenshots
![ss1](<screenshots/Screenshot 2025-11-23 165635.png>)
![ss2](<screenshots/Screenshot 2025-11-23 165801.png>)
![ss3](<screenshots/Screenshot 2025-11-23 165855.png>)
