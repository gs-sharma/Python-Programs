import time                                     #for time sleep
from datetime import datetime as dt             #for date and time from pc

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
temp_host = r"C:\Users\Gourav\Desktop\Learn\python\website-blocker\hosts"
website_list=["www.facebook.com", "facebook.com" , "gmail.com" ]

while True:                                    #so that the program runs cotiniously
    # to compare the current time with our condition
    if (dt(dt.now().year , dt.now().month , dt.now().day , 8)) < dt.now() < (dt(dt.now().year , dt.now().month , dt.now().day , 12)):
        print("working Hours...")
        with open(host_path, 'r+') as file:
            content=file.read()                  #all data as a single list element
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("fun hours")
        with open(host_path, 'r+') as file:
            content=file.readlines()          #each line as a single list element
            file.seek(0)                      #to place the cursor at the start of file
            for line in content:
                if not any(website in line for website in website_list):   #check if website name is present in line or not
                    file.write(line)                                       #if not than print lines
            file.truncate()                                                #delete all the contents after the cursor
    time.sleep(5)                                                          #run while loop every 5 sec
