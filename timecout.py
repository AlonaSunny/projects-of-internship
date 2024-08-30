import time
t=int(input("enter countdown in secs"))
def countdown(t):
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end='\r')
        time.sleep(2)
        t-=1
    print("OK")
countdown(t)
