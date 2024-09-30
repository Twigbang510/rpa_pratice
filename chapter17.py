# Chapter 17: Keeping Time, Scheduling Tasks, and Launching Programs

import time
import datetime
import subprocess
import schedule

# 1. Getting the Current Time
def get_current_time():
    current_time = time.time()
    print(f"Current time in seconds since the epoch: {current_time}")  # Output: Current time in seconds since the epoch: 1633036800.0

    local_time = time.ctime()
    print(f"Local time: {local_time}")  # Output: Local time: Sun Sep 30 10:00:00 2024

# 2. Working with datetime Module
def datetime_operations():
    current_datetime = datetime.datetime.now()
    print(f"Current date and time: {current_datetime}")  # Output: Current date and time: 2024-09-30 10:00:00

    specific_datetime = datetime.datetime(2024, 9, 30, 10, 0)
    print(f"Specific date and time: {specific_datetime}")  # Output: Specific date and time: 2024-09-30 10:00:00

    time_difference = current_datetime - specific_datetime
    print(f"Time difference: {time_difference}")  # Output: Time difference: 0:00:00

# 3. Pausing the Program with time.sleep()
def pause_program():
    print("Pausing for 3 seconds...")
    time.sleep(3)
    print("Resumed.")  # Output: Resumed.

# 4. Scheduling Tasks
def scheduled_task():
    print("Task executed at:", datetime.datetime.now())  # Output: Task executed at: 2024-09-30 10:03:00

def schedule_tasks():
    # Schedule the `scheduled_task` to run every minute
    schedule.every(1).minutes.do(scheduled_task)

    print("Scheduler running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)

# 5. Launching Programs with subprocess
def launch_program():
    print("Launching Calculator...")
    try:
        # Launching a calculator application
        subprocess.Popen('calc')  # Windows example, replace 'calc' with a different command for other OS
    except FileNotFoundError:
        print("Calculator application not found.")  # Output: Calculator application not found.

# 6. Practice Project: Countdown Timer
def countdown_timer(seconds):
    print(f"Countdown starts for {seconds} seconds.")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f'{mins:02d}:{secs:02d}'
        print(timer_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Countdown finished!")  # Output: Countdown finished!
    
# 7. Practice Project: Alarm Clock
def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! It's time!")
            subprocess.Popen(['start', 'test.wav'], shell=True)
            break
        time.sleep(1)
