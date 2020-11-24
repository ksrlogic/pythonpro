from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from tagParse import tagParse
from getHT import getHT
from evaluate import evaluate
import re

from operator import itemgetter


def login(id, password, driver):
    driver.get('https://everytime.kr/login')
    driver.find_element_by_name('userid').send_keys(id)
    time.sleep(0.5)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

def getData(driver):
    driver.get('https://everytime.kr/timetable')
    time.sleep(0.5)
    html = driver.page_source
    soup = bs(html, 'lxml')
    tables = soup.find('table', 'tablebody').find_all('td')
    timetable = []

    for table in tables:
        datas = table.find_all('div',  {"class": "cols" })
        for data in datas:
            onlyDiv = tagParse(str(data))
            daytime = []
            for div in onlyDiv:
                if div.startswith('<'):
                    daytime.append(div)
            timetable.append(daytime)
    print(timetable)    
    return timetable

def getCredit(driver):
    driver.get('https://everytime.kr/timetable')
    time.sleep(0.5)
    html = driver.page_source
    soup = bs(html, 'lxml')
    score = str(soup.find(id="tableCredit"))
    score = re.sub('<.+?>', '', score, 0).strip()

    return score

def clear(timetable):
    realTimeTable = []
    for day in timetable:
        daytable = []
        for schedule in day:
            HT_TUPLE = getHT(schedule)
            daytable.append(HT_TUPLE)
        realTimeTable.append(sorted(daytable,key=lambda x: x[0], reverse=False)) #Time Sorting
    
    return realTimeTable


