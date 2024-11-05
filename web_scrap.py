from encodings.utf_16 import encode
from http.client import responses

import requests
from bs4 import BeautifulSoup
import json


url = "https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/?ref=lbp"

page = requests.get(url)
status = page.status_code
soup = BeautifulSoup(page.content, "html.parser")

data = soup.find("table").text
datas = data.encode()


with open('data.json','wb') as f:
    f.write(datas)
    f.close()

# print(status)
# print(page.text)