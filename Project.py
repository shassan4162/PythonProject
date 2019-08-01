# Download All Data
# Import libraries
import requests 
import os
import urllib.request
from bs4 import BeautifulSoup


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

os.makedirs('2019/01')
os.makedirs('2019/02')
os.makedirs('2019/03')
os.makedirs('2019/04')
os.makedirs('2019/05')
os.makedirs('2019/06')
os.makedirs('2019/07')
os.makedirs('2019/08')
os.makedirs('2019/09')
os.makedirs('2019/10')
os.makedirs('2019/11')
os.makedirs('2019/12')





# ---- Yearly Folder Script with Opposite Pattern----
# Import libraries
import requests 
import urllib.request
from bs4 import BeautifulSoup
import os

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

# do not know request number yet
request_number = ''

# base dir
_dir = "C:\Python Project"       

# create dynamic name, like "C:\Python Project\File82673"
_dir = os.path.join(_dir, 'File%s' % request_number)

# create 'dynamic' dir, if it does not exist
if not os.path.exists(_dir):
    os.makedirs(_dir)

os.makedirs('2019/01')
os.makedirs('2019/02')
os.makedirs('2019/03')
os.makedirs('2019/04')
os.makedirs('2019/05')
os.makedirs('2019/06')
os.makedirs('2019/07')
os.makedirs('2019/08')
os.makedirs('2019/09')
os.makedirs('2019/10')
os.makedirs('2019/11')
os.makedirs('2019/12')

