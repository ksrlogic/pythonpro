from getData_Selenium import getData, clear
from driver import driver

def dataParse(driver):
    table = getData(driver)
    timetable = clear(table)
    return timetable