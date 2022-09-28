# Automation using python 🤖🧰:
![image](https://user-images.githubusercontent.com/112848881/192870467-631c51b6-0740-4b76-9ba0-4ad41d9550c9.png)

# Course content:
* Introduction to web scraping
* Setting up the environment
* Project architecture overview
* Building Hacker news scraper
* Sending Email from python
* Building the headlines Email Module

# Introduction to Web Scraping 📝:

# . Things we are going to do:
* Get HN website front page
* Scrape required content
* Build Email body/content
* Email Authentication 
* Email sent

# Note:
We are extracting content from web page, then we are going to take the required components and use the email body in the email that we compose
and then we send it to required users.

# Setting up Python Enivironment 🏡:
# Packages:
* requests: used for HTTP requests
* bs4: beautiful soup used for web scraping
* smttplib(default): Email authentication and transaction
* email.mime(default): creating email body
* datetime(default): accessing and manipulating date and time
![image](https://user-images.githubusercontent.com/112848881/192851529-e57f9239-2fd8-4fe1-b4c0-b82cd129852c.png)

# Website structure of Hackernews FrontPage 🕸:
```python
import requests       # http requests
from  bs4 import BeautifulSoup       # web scraping
import smtplib     # send the mail

# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

# Extracting Hacker News Stories

content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ("<b>HN Top Stories:</b>\n"+'<br>'+'-'*50 +'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class': 'title', 'valign':''})):
        cnt += ((str(i+1)+ '::' +tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return (cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

```
# Sending Email from python 📩😳:
![image](https://user-images.githubusercontent.com/112848881/192870715-db252f4e-10cc-484a-8d83-df0c109d4149.png)

```python
import requests       # http requests
from  bs4 import BeautifulSoup       # web scraping
import smtplib     # send the mail

# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

# Extracting Hacker News Stories

content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ("<b>HN Top Stories:</b>\n"+'<br>'+'-'*50 +'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class': 'title', 'valign':''})):
        cnt += ((str(i+1)+ '::' +tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return (cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# Lets send the email
print("Composing Email...")
# update ur email details
SERVER = 'fantasmaamante09@gmail.com'
PORT = 587
FROM = 'fantasmaamante09@gmail.com'
TO = 'fantasmaamante09@gmail.com'
PASS = '*****'

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + '' + str(now.day) + '-' + str(
now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content,'html'))

print('Intitiating Server...')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print('Email Sent...')

server.quit()
```
* 🔚

