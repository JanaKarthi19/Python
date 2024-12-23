import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import sqlite3

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.titleline')
scores = soup.select('.subtext')

res2 = requests.get('https://news.ycombinator.com/?p=2')
soup2 = BeautifulSoup(res2.text,'html.parser')
links2 = soup2.select('.titleline')
scores2 = soup2.select('.subtext')


Mega_links = links + links2
Mega_scores = scores + scores2


def sorted_Data(hnlist):
    return sorted(hnlist, key=lambda k:k['Votes'], reverse=True)

def created_hn(links, scores):
    hn = []
    hr =[]
    for idx, item in enumerate(links):
        title = links[idx].a.getText()
        href = links[idx].a.get('href')
        points = scores[idx].select('.score')
        if len(points):
            votes = int(points[0].getText().replace('points',''))
            if votes > 99:
                hn.append({'Title':title,'Link':href,'Votes':votes})
    return sorted_Data(hn)

print(type(created_hn(Mega_links,Mega_scores)))

                # Saving into Different File types

start = created_hn(Mega_links,Mega_scores)

title = []
link = []
vote = []

keys = 'Title'
key2 = 'Link'
key3 = 'Votes'

for x in start:
    if keys in x and key2 in x and key3 in x:
        title.append(x[keys])
        link.append(x[key2])
        vote.append(x[key3])

Data = {'title':title,'Link':link,'Voted':vote}

df = pd.DataFrame(Data)
# print(df)

# Storing into CSV File

df.to_csv('Hacker_News.csv',index=False)

# Storing into Excel File

df.to_excel('Hacker_News.xlsx', index=False)

# Storing into Database File using sqlite3

connection = sqlite3.connect('Hacker_News.db')
cursor = connection.cursor()
query='CREATE TABLE IF NOT EXISTS News(Title, Links, Votes)'
cursor.execute(query)


for i in range(len(df)):
    cursor.execute("INSERT INTO News values(?,?,?)",df.iloc[i])

connection.commit()
connection.close()
print('Datas are successfully stored into Database')




