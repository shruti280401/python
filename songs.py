import re
import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/List_of_songs_recorded_by_Arijit_Singh"
req = requests.get(url)
soup = BeautifulSoup(req.text,'lxml')
title = soup.findAll('tr')
#for t in  title:
    #print(t)
file=open("C:\\Users\Dell\OneDrive\Desktop\py files\\song.txt","w",encoding="UTF-8")
for t in title:
    s=str(t)
    file.write(s)
    #print(s)
file.close()
file=open("C:\\Users\Dell\OneDrive\Desktop\py files\\song.txt","r")
newli=[]
for s in file.readlines():
     if s.startswith("<th"):
         r = re.findall("<i><a.+>(.+)</a>",s)
         newli.append(r)

     if s.startswith("<td"):
         f = re.findall("<td>(.+)",s)
         newli.append(f)
print(newli)
file.close()
