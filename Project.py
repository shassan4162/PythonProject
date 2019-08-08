# Download All Data
# Import libraries
import requests 
import os
import urllib.request
from bs4 import BeautifulSoup
os.mkdir('All Data') 
import shutil
import fnmatch


# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 

src = 'turnstile_190803.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190727.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190720.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190713.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190706.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190629.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190622.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190615.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190608.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190601.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190525.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190518.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190511.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

for filename in os.listdir('All Data'):
    if fnmatch.fnmatch(filename, 'turnstile_1908**.txt'):
        print(filename)








# ---- Yearly Folder Script with Opposite Pattern----
# Import libraries
import requests 
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import fnmatch

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download only 2019 data
for i in range(36,len(soup.findAll('a'))-1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')-1:]) 


# create 'dynamic' dir, if it does not exist
if not os.path.exists('All Data'):
    os.makedirs('All Data')

#Copying file to 'All Data" Directory
src = 'turnstile_190803.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190727.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190720.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190713.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190706.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190629.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190622.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190615.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190608.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190601.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190525.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190518.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

src = 'turnstile_190511.txt'
dst = 'C:/Users/user/Desktop/Python/All Data'
shutil.copy(src, dst)

#Creating sub folder in Directory 'All Data'
for filename in os.listdir('All Data'):
    if fnmatch.fnmatch(filename, 'turnstile_1908**.txt'):
        print(filename)

