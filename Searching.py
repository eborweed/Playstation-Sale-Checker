from math import e
from queue import Empty

#from sys import exception


class Searchbar():
  def Searchbar(gamename):    
    names=[]
    images=[]
    prices=[]
    oldPrice=[]
    links=[]
    import time
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    path= r"C:\Users\ibrah\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    s=Service(r"C:\Users\ibrah\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    chromeoptions= Options()
    chromeoptions.headless=True
    chromeoptions.add_experimental_option("detach", True)
    website="https://store.playstation.com/en-nz/pages/latest"
    driver=webdriver.Chrome(path,options=chromeoptions)
    driver.get(website)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="shared-nav"]/span/span/button').click()
    driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/input').send_keys(gamename)
    driver.find_element_by_xpath('/html/body/div[7]/div/div/div/button[2]').click()
    time.sleep(1)
    prices= driver.find_elements_by_class_name("psw-m-r-3")
    gamenum=(driver.find_element_by_xpath('//*[@id="main"]/section/div/p/span[1]/span').text)
    gamenum=int(str.split(gamenum)[-1])
    if gamenum>8:   
     gamenum=8
    for i in range(0,gamenum):    
     try:     
      names.append(driver.find_element_by_xpath(f'//*[@id="main"]/section/div/ul/li[{i+1}]/div/a/div/section/span[2]').text)
      images.append(driver.find_element_by_xpath(f'//*[@id="main"]/section/div/ul/li[{i+1}]/div/a/div/div/div[1]/span[2]/img[2]').get_attribute("src"))
      links.append(driver.find_element_by_css_selector(f'#main > section > div > ul > li:nth-child({i+1}) > div > a').get_attribute("href"))    
     except:    
      names.append(driver.find_element_by_xpath(f'//*[@id="main"]/section/div/ul/li[{i+1}]/div/a/div/section/span').text)
      images.append(driver.find_element_by_xpath(f'//*[@id="main"]/section/div/ul/li[{i+1}]/div/a/div/div/div[1]/span[2]/img[2]').get_attribute("src"))
      links.append(driver.find_element_by_css_selector(f'#main > section > div > ul > li:nth-child({i+1}) > div > a').get_attribute("href"))
     try:     
      oldPrice.append(driver.find_element_by_css_selector(f"s[data-qa='search#productTile{i}#price#price-strikethrough']").text)
      if "$" not in oldPrice[i]:    
       print(oldPrice[i])
       oldPrice[i]= ""    
     except:    
      oldPrice.append("")   
    return names , images , prices , oldPrice ,links, gamenum   