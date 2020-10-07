from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from tagParse import tagParse
from getHT import getHT
from evaluate import evaluate
import stdiomask

id = input("아이디를 입력해주세요: ")
password = stdiomask.getpass()

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://everytime.kr/login')

driver.find_element_by_name('userid').send_keys(id)
time.sleep(0.5)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

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
                print(div)
                daytime.append(div)
        print("============")
        timetable.append(daytime)

print(timetable)
print("===============")

realTimeTable = []

from operator import itemgetter

for day in timetable:
    daytable = []
    for schedule in day:
        HT_TUPLE = getHT(schedule)
        daytable.append(HT_TUPLE)
    realTimeTable.append(sorted(daytable,key=lambda x: x[0], reverse=False)) #Time Sorting

print(realTimeTable)

evaluate(realTimeTable)

driver.quit()