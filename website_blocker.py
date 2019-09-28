import time
from datetime import datetime as dt

host_temp="hosts"
hosts_path=r"/etc/hosts"
redirect="127.0.0.1"
website_list=["www.xvideos.com","www.tubxporn.com","www.xvideos2.com","www.xnxx.com","www.pornhub.com","www.xhamster.com","www.redtube.com","www.youporn.com","www.naughtyamerica.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours....")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    file.truncate()
        print("Fun hours.....")
        time.sleep(5)
