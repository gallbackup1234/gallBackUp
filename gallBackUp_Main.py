import requests
from bs4 import BeautifulSoup
import codecs
import html
import os.path
import errno

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
headers = {'User-Agent': user_agent}
url = 'https://gall.dcinside.com/mgallery/board/view/?id=lastorigin&no=1384131'
url_get = requests.get(url, headers=headers)
html_code = url_get.content.decode('utf-8')
soup = BeautifulSoup(html_code, 'html.parser')
established_date = soup.find('span', {'class' : 'gall_date'}).get('title')[0:10]
title_article = soup.find('span', {'class' : 'title_subject'}).getText()
contents_article = soup.find('div', {'class' : 'writing_view_box'})
folder_name = established_date + ' ' + title_article

try:
    if not(os.path.isdir(folder_name)):
        os.makedirs(os.path.join(folder_name))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory")
        raise

filepath = os.path.join(folder_name, 'contents.html')
with codecs.open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(contents_article))
