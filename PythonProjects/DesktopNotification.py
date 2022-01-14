import time
from plyer import notification

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = '/media/janeki/Linux Storage/Developing../Python/ManualReviewerProject/BetterIcon.ico',
        
        timeout = 10,
    )
    

if __name__ == "__main__":
    while True:
        notifyMe('Hey you sit for too long!','Do some exercise and walk a little for now!')
        time.sleep(10)