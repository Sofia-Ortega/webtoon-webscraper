import time
from bs4 import BeautifulSoup
import requests
from constants import FAKE_URL
from datetime import datetime, timedelta


def getTime():
    t = time.localtime();

    current_day = datetime(t.tm_year, t.tm_mon, t.tm_mday)
    current_time = time.strftime("%H:%M:%S", t)

    return {
        "day": current_day,
        "hour": current_time,
    }


def strToInt(str):
    million = False

    if( "M" in str ):
        str = str.replace("M", "")
        million = True
    
    result = float(str.replace(',', ''))
    
    if(million): result = result * 1000000

    return int(result)


def webscraper(url):

    # setup
    # resp = requests.get(url)
    # soup = BeautifulSoup(resp.text, "html.parser") #FIXME

    with open(FAKE_URL) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    # get title
    title = soup.title.text
    title = title.split(' |', 1)[0].replace(' ', '_')

    # get tags
    tag = soup.find('ul', {"class": "grade_area"})
    datas = tag.find_all("li")
        
    data = {
        "views": -1,
        "subscribers": -1,
        "grade": -1.0 
    }


    data["views"] = strToInt(datas[0].em.text) 
    data["subscribers"] = strToInt(datas[1].em.text)
    data["grade"] = float(datas[2].em.text)

    results = {
        "title": title,
        "data": data,
        "timestamp": getTime()
    }

    return results


