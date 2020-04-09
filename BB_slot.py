import bs4

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities     
import sys
import time
import os


def getWFSlot(productUrl):
   
   driver = webdriver.Chrome(executable_path = "./chromedriver")
   driver.get(productUrl)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)
   time.sleep(25)
   no_open_slots = True



   while no_open_slots:
      driver.get(productUrl)           
      print("refreshed")
 
      time.sleep(4)
      try:
         driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[3]/div[2]/div/div[6]/div[1]/div[1]/button").click()
         html = driver.page_source
         soup = bs4.BeautifulSoup(html)
         print driver.current_url
         if "checkout" in driver.current_url:
            print "YEP!"
            os.system('say "Slots for delivery opened!"')
            time.sleep(600)
      except:
         print "nope"
         pass


getWFSlot('https://www.bigbasket.com/basket/?ver=1')
# getWFSlot('https://www.bigbasket.com/')


