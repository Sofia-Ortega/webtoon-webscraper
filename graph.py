from webscrape import webscraper
from csv import writer, reader
from constants import FILENAME, URL

def writerows(rows, filename):
    with open(filename, 'a', encoding='utf-8') as toWrite:
        w = writer(toWrite)
        w.writerows(rows)
        toWrite.close()

def parseData(data):
    filename = "webtoonData/" + data["title"] + ".csv"
    dataArr = [data["data"]["views"], data["data"]["subscribers"], data["timestamp"]["day"], data["timestamp"]["hour"]]
    print(dataArr)

def readData(webtoonName, ):
    fileName = "webtoonData/" + webtoonName + ".csv"
    time = []
    subscribers = []

    with open(fileName, 'r') as file:
        csvreader = reader(file)
        for row in csvreader:

            

parseData(webscraper(URL))

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
plt.style.use('seaborn')


x = []
y = []

with open("dayData.csv", 'r') as file:
    csvreader = reader(file)
    for row in csvreader:
        x.append(row[0].split(' ', 1)[0])
        y.append(row[1])

plt.plot_date(x, y)
plt.tight_layout()
plt.show()