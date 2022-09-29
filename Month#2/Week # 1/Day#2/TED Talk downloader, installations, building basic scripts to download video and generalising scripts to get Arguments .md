# Building TED Talk video downloader:
  # Steps required:
  * Installation and Introduction to request packages
  * Building the basic script to download the video
  * Generalising the scripts to get arguments
  * Packaging the script as a CLI tool
  
  # Installations:
  ![image](https://user-images.githubusercontent.com/112848881/193060674-68279eb1-5526-4b3c-9315-941f39e512e3.png)

  # Building basic script to download the video:
  ```python
  import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

r = requests.get(url)
print("Download about to start")

soup = BeautifulSoup(r.content, features='lxml')
for val in soup.find_all("script"):
    if(re.search("talkpage.init",str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?:[^\s]+)(mp4)", result).group("url")
mp4_url = result_mp4.split('"')[0]
print("Downloading video from ....." + mp4_url)
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]
print("Storing video in ..... " + file_name)

r = requests.get(mp4_url)
with open(file_name,'wb') as f:
    f.write(r.content)

print("Download process finished")
# ted_talk_downloader.py
  ```
