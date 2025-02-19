import time
from plyer import notification
def drink_water_reminder():
    title = "Drink Water Reminder"
    message = "It's time to drink some water!"
    notification.notify(title, message)
def main( ):
    while True:
        time.sleep(1200)
        drink_water_reminder()
if  __name__ == '__main__':
    main( )