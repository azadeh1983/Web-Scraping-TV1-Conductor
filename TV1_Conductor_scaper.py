from bs4 import BeautifulSoup
import requests

import datetime
import time
import csv

URL = 'https://tv1.ir/Conductor'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers=headers)

Soup1 = BeautifulSoup(page.content, "html.parser")
Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")

titleList=[]
timeplayList=[]
timeduringList =[]

title = Soup2.find_all( "h5",class_='titlecls')
timeplay=Soup2.find_all("div",class_='text- text-xs-left font-size-12')
timed=Soup2.find_all("span",class_='extracls')

for v in title:
    titleList.append(v.get_text().strip())

for t in timeplay:
    timeplayList.append(t.get_text().strip())

for d in timed:
    timeduringList.append(d.get_text().strip())


# To obtain current date and time
date = datetime.date.today()
t = time.localtime()

current_time = time.strftime("%H:%M:%S",t)
print(date)
print(current_time)


# write in file
header = ['Title','Time of Play','Description','current_date','current_time']
data = [titleList, timeplayList,timeduringList,date,current_time]

# Writing the data we scraped into a csv file
with open ("tv1_Conductor.csv",'w',newline='',encoding='UTF8') as f:
    writingdata = csv.writer(f)
    writingdata.writerow(header)
    writingdata.writerow(data)

print(titleList)
print(timeplayList)
print(timeduringList)
