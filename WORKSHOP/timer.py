import time

def timer(min):
    seconds = min *60

    while seconds>0:
        print("Time remaining: ",seconds,end='\r')
        time.sleep(1)
        seconds -=1
    print("Time up!")

timer(5)