from re import X
import time
import os
os.system('clear')
SB =open("Sender_Buffer.txt", "a+")
RB =open("Reciever_Buffer.txt" , "r+")
SB.truncate(0)
RB.truncate(0)
ws = int(input("Enter Window size:"))
s = input("Enter Input String:")
s = list(s)
if(ws<len(s)):
    for i in range(0,len(s),ws):
        p=s[i:i+ws]
        y=s[i+ws:i+ws+ws]
        print("Sent->"+str(p))
        time.sleep(ws)
        print("Sending->",str(y))
        x=0
        while(x<ws):
            time.sleep(2)
            if(len(p)>x):
                print("ACK~!",p[x],"!")
                RB.write(p[x])
            time.sleep(1)
            if(len(y)>x):
                print("Sending->",y[x])
                SB.write(y[x])
            x+=1
else:
    print("~>The window size is too large.")
