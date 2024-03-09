from Searching import Searchbar
import GUI
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#path= r"C:\Users\ibrah\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
#s=Service(r"C:\Users\ibrah\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#chromeoptions= Options()
#chromeoptions.headless=True
#website="https://store.playstation.com/en-nz/concept/10001555"
#
#driver=webdriver.Chrome(path,options=chromeoptions)
#
#driver.get(website)
#time.sleep(1)
#matches= driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/label/div/span/span/span')
#driver.get_screenshot_as_file("screenshot.png")
#print(matches.text)
GUI.main()
