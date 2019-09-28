import requests as re
from bs4 import BeautifulSoup
import os

def checkCreatePath(directory):
    #it will only create a directory if its not available
    if not os.path.exists(directory):
        #function responsible 
        os.makedirs(directory)
        print("[>]"+directory+"Folder Created")

       
#create sub directories 
def create_sub_directories(year,month,date):
    checkCreatePath(str(year))
    checkCreatePath(str(year)+"/"+str(month))
    checkCreatePath(str(year)+"/"+str(month)+"/"+str(date))

Page=re.get("http://web.mta.info/developers/turnstile.html")
parser = BeautifulSoup(Page.content, 'html.parser')            
content=parser.find('div',class_='span-84 last')

files=content.findAll('a')

#loop to find all tags
for i in files:

	print(i['href'].ljust(40)+"   "+i.text)
	year=i.text.split(',')[2].strip()
	month,day=i.text.split(',')[1].split()
	directory=year+"/"+month+"/"+day+"/"
	create_sub_directories(year,month,day)

	url=i['href']
	file_name=url.split('/')[-1]
	link="http://web.mta.info/developers/"+url

	content=re.get(link).text
    #print(directory+file_name)
	open(directory+file_name,'w',encoding='utf-8').write(content)
    
#Visual Studio code was the code editor, solution is written in python 3.2
#To see the created changes see the directory path to where Visual Studio Code is linked to, for example for me it was in desktop folder
#in a folder named 'python' 
