import urllib.request
from pdfminer.high_level import extract_text
import requests
import re


# send message to your line 
def send_line(msg):
    endpoint = "https://notify-api.line.me/api/notify"
    data = {"message": msg}
    headers = {"Authorization": "Bearer your_line_authorization_key"}
    x = requests.post(endpoint, data=data, headers=headers)
    print(x.json())

# download from website, website requires a user agent to allow download
def download(url, local):
  opener=urllib.request.build_opener()
  opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
  urllib.request.install_opener(opener)

  urllib.request.urlretrieve(url,local)
  print("pdf downloaded")

url = 'https://www.chp.gov.hk/files/pdf/building_list_eng.pdf'
local= './download/covid/building.pdf'
download(url, local)
text = extract_text(local)
print("text extracted")

# use re to find a match of building name or street name
if re.search('building name', text, re.IGNORECASE) or re.search('or street name', text, re.IGNORECASE):
  send_line('Found a match! check https://www.chp.gov.hk/files/pdf/building_list_eng.pdf')
else:
  print("relax... no match")
