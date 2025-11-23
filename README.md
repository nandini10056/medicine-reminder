
# Smart Medicine Reminder System

This Smart Medicine Reminder System is a Python-based application that helps users remember their daily medication. The program allows users to store medicine names and timings, then sends reminders through notifications at the scheduled time. It is simple, practical, and solves a real-life problem of forgetting medicines.

## Features

* Add medicines with specific times (HH:MM format)

* View the entire medicine schedule

* Automatic reminders

* Data stored permanently in medicines.txt

## Technologies Used

* Python 3

* Libraries:

   * time – for time checking
   * os – file handling
   * datetime - for handling time calculations

## How to Run
1. Run the program: medicine_reminder.py
2. Keep the program running to receive reminders.

## How It Works

1. User chooses from menu:
   * Add medicine
   * View schedule
   * Exit



2. When a medicine is added:
    * Name and time are stored in a txt file



3. A background loop:

    * Checks current time every minute
    * Compares with stored times

## Real-Life Use
* Helps patients taking regular medicine
* Useful for school/college students
* Helpful for elderly people