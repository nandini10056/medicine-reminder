import time
from datetime import datetime
import os

MEDICINE_FILE = "medicines.txt"
LOG_FILE = "medicine_log.txt"

def add_medicine():
    name = input("Enter medicine name: ")
    interval = int(input("Enter interval (hours): "))
    start_time = input("Enter first dose time (HH:MM): ")

    with open(MEDICINE_FILE, "a") as f:
        f.write(f"{name},{interval},{start_time}\n")

    print("\nMedicine added successfully!\n")

def load_medicines():
    medicines = []

    if not os.path.exists(MEDICINE_FILE):
        return medicines

    with open(MEDICINE_FILE, "r") as f:
        for line in f:
            if line.strip():
                name, interval, start = line.strip().split(",")
                medicines.append({
                    "name": name,
                    "interval": int(interval),
                    "start": start
                })
    return medicines

def log_dose(medicine_name):
    with open(LOG_FILE, "a") as f:
        f.write(f"Reminder: {medicine_name} at {datetime.now().strftime('%H:%M')} on {datetime.now().date()}\n")

def reminder_loop():
    print("\n Reminder system started... (Press CTRL + C to stop)\n")
    medicines = load_medicines()

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        for med in medicines:
            start_dt = datetime.strptime(med["start"], "%H:%M")
            interval_hours = med["interval"]

            delta = now - now.replace(hour=start_dt.hour, minute=start_dt.minute, second=0, microsecond=0)

            hours_passed = delta.total_seconds() // 3600

            if hours_passed % interval_hours == 0 and now.minute == start_dt.minute:
                print(f"\n Time to take your medicine: {med['name']} ({current_time})")
                log_dose(med["name"])

        time.sleep(60)  

def main():
    
    while True:
        print("\n Smart Medicine Reminder ")
        print("1. Add Medicine")
        print("2. Start Reminder System")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_medicine()
        elif choice == "2":
            reminder_loop()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()