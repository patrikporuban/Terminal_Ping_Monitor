from pythonping import ping
from termcolor import colored
from datetime import datetime
import winsound

Min = 50
Max = 100

i=0
#iMin = 0
iMid = 0
iMax = 0

while(True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S -> ")

    i+=1
    response_list = ping('google.com', size=40, count=10)
    if(response_list.rtt_avg_ms<Min):
        print("[{}]".format(i),current_time,"Ping is: ",colored(response_list.rtt_avg_ms, 'green'),"ms")
        #winsound.Beep(2500, 50)
        #iMin+=1
    elif(response_list.rtt_avg_ms<Max and response_list.rtt_avg_ms>=Min):
        print("[{}]".format(i),current_time,"Ping is: ",colored(response_list.rtt_avg_ms, 'yellow'),"ms")
        winsound.Beep(2000, 50)
        iMid+=1
    elif(response_list.rtt_avg_ms>=Max):
        print("[{}]".format(i),current_time,"Ping is: ",colored(response_list.rtt_avg_ms, 'red'),"ms")
        winsound.Beep(2200, 25)
        winsound.Beep(2200, 25)
        iMax+=1
    if(i>=500):
        if(iMax>20 or iMid>50):
            print(colored("Internet is not ready for gaming","red"))
            x = input("Do you want to repeat test ? 1 - continue, 0 - stop")
            if(x==1):
                iMax=0
                iMid=0
                i=0
            else:
                break
        else:
            print(colored("Mid: {} Max: {}".format(iMid,iMax),"green"))
            iMax=0
            iMid=0
            i=0