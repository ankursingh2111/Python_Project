import time
from datetime import datetime as dt

host_temp="hosts"
host_main="/etc/hosts"

redirect="127.0.0.1"
web_block=["facebook.com","www.facebook.com","gmail.com","www.gmail.com","mail.google.com"]

while 1:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23):
        print ("Working hours")
        with open(host_main,"r+") as filehandle:
            content=filehandle.read()
            for web in web_block:
                if web in content:
                    pass
                else:
                    filehandle.write(redirect + "    " + web + "\n")
    else:
        print("Fun hours")
        with open(host_main,"r+") as filehandle:
            content=filehandle.readlines()
            filehandle.seek(0)
            for line in content:
                #print(line)
                if not any(web in line for web in web_block):
                    filehandle.write(line)
            filehandle.truncate()
    time.sleep(10)
