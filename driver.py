from selenium import webdriver
from getData_Selenium import login
import os
path = os.getcwd()
driverUrl = path.replace('\\', '/') + "/chromedriver.exe"
print(driverUrl)
driver = webdriver.Chrome("C:/Users/winco/Desktop/ABC/chromedriver.exe")