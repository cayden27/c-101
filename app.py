import time

seconds = input("enter time in number of seconds")

def countdown_timer(seconds):
    while seconds > 0:

        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'                    
        print(timer)

        seconds -= 1
    print("times up")

countdown_timer(int(seconds))