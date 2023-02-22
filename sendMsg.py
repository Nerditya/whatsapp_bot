from twilio.rest import Client
import requests
import json
import os
from random import choice
import meme
import game
file=open("a.txt","r")
f=file.read()
sid=''#fill after registering on twilo
authToken=''
client =Client(sid,authToken)

debtlist={}
file.close()
events={}
notes =[]
# print(debtlist)
import time
def send(msg):
    message= client.messages.create(to='whatsapp:+917057070497',from_='whatsapp:+14155238886',body=msg)
def action(cmd):
    if cmd=='dog':
        response_API = requests.get('https://dog.ceo/api/breeds/image/random')
        r=response_API.json()
        message = client.messages.create(body='Check out this funny picture!',
                       media_url=r['message'],
                       from_='whatsapp:+14155238886',

                       to='whatsapp:+917057070497')
    elif cmd[0:2]=='ex':
        st=""
        i=2
        while cmd[i]!=" ":
            st=st+cmd[i]
            i=i+1
        

        st=int(st)
        i= i+1
        name=cmd[i:]
        print(name)
        if name not in debtlist:
            debtlist[name]=st
        else:
            debtlist[name]+= st

    elif cmd=='printdebt':
        s=""
        for p in debtlist: 
            s=s+str(p)+":"+str(debtlist[p])+'\n'

        send(s)
    elif cmd[0:2]=='py':
        st=cmd[2:]
        fil1= open("pcode.txt","w+")
        fil1.write("f=open('out.txt','w+')\n")
        fil1.write(st)
        fil1.write("\nf.close()")

        base = os.path.splitext("pout.txt")[0]
        os.rename("pcode.txt", base + '.py')
        # os.rename("pcode.txt","pcode.py")
        os.system("pcode.py")
        # os.rename("pcode.py","pcode.txt")
        base = os.path.splitext("pcode.py")[0]
        os.rename("pout.py", base + '.txt')
        fil2=open("out.txt",'r')
        s=fil2.read()
        print(s)
        send(s)
        fil2.close()

    elif cmd=='tt':
        
        message = client.messages.create(body='Time Table',
                       media_url='https://www.linkpicture.com/view.php?img=LPic63f373cc297001612504667',
                       from_='whatsapp:+14155238886',

                       to='whatsapp:+917057070497')
    elif cmd[0:7]=='algebra':
        s=cmd[7:]
        send(str(eval(s)))

    elif cmd[0:2]=='ev':
        
        st=""
        i=2
        while cmd[i]!=" ":
            st=st+cmd[i]
            i=i+1
        

        st=int(st)
        i= i+1
        name=cmd[i:]
        print(name)
        if name not in debtlist:
            events[name]=st
        else:
            events[name]+= st
    elif cmd=='prevents':
        s=str(events)
        send(s)

    elif cmd[0:4]=='note':
        s=cmd[4:]
        notes.append(s)
    elif cmd=='printnotes':
        s=""
        no=1
        for note in notes:
            s=s+str(no)+". "+note+'\n'
            no=no+1

        send(s)
    elif cmd=='pls meme':
        ur= choice(meme.memer())
        print(ur)
        message = client.messages.create(body='',
                       media_url=ur,
                       from_='whatsapp:+14155238886',

                       to='whatsapp:+917057070497')
    elif cmd[0:6]=='pls r/':
        a= cmd[6:]

        try:
            ur = (choice(meme.imgs(a)))
            print(ur)
            message = client.messages.create(body='',
                            media_url=ur,
                            from_='whatsapp:+14155238886',

                            to='whatsapp:+917057070497')
        except:
            message = client.messages.create(body='Nothing Much We GOT :-<',
                       
                       from_='whatsapp:+14155238886',

                       to='whatsapp:+917057070497')
    elif cmd[0:9]=='game_tnd ': 
        a=cmd[9:]
        s=game.tnd(a)
        send(s)



    
            
    # elif cmd[0:3]=="img":
    #     sp=cmd[3:]
    #     response_API = requests.get('https://+'+sp+'.ceo/api/random')
    #     r=response_API.json()
    #     message = client.messages.create(body='Check out this funny picture!',
    #                    media_url=r['message'],
    #                    from_='whatsapp:+14155238886',

                    #    to='whatsapp:+917057070497')









    

        






        


# print(messages)
a=""
message = client.messages.create(body='Check out this funny picture!',
                       media_url='https://raw.githubusercontent.com/dianephan/flask_upload_photos/main/UPLOADS/DRAW_THE_OWL_MEME.png',
                       from_='whatsapp:+14155238886',
                       to='whatsapp:+917057070497')
                       
msrecieved=['i']
while True:
    
    time.sleep(1)
    messages= client.messages.list(limit=5)
    if a!=messages[0].body:
        a=messages[0].body
        # msrecieved.append(a)
        action(a)
        print(a)
        # print(msrecieved)
        s=str(debtlist)
        file=open("a.txt","w+")
       
        file.write(s)
        



    
