from selenium import webdriver
import sys
import time
import os
import datetime
import requests

def get_bb_slot(url):
    # auto-install chromedriver 
    driver = webdriver.Firefox()
    driver.get(url)
    print("Please login using OTP and then wait for a while.")
    time.sleep(60)


    while 1:
        driver.get(url)     
        time.sleep(2)
        currentTime = datetime.datetime.now()
        print(currentTime.strftime("%Y-%m-%d %H:%M:%S") + "  Trying to find a slot!")
        try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()
            time.sleep(5)  #driver take a few sec to update the new url
            src = driver.page_source
            if "checkout" in driver.current_url and not "Unfortunately, we do not have" in src:
                currentTime = datetime.datetime.now()
                print(currentTime.strftime("%Y-%m-%d %H:%M:%S") + "  Found the slots!")
                for i in range(60):
                     notify("Slots Available!", "Please go and choose the slots!")
                     telegram = "https://api.telegram.org/bot1226998212:AAHWi9dI6lbQmKWvj4b-sFZ1JZeX8-m4EFQ/sendMessage?chat_id=1105404285&parse_mode=Markdown&text=Slots Found!"
                     requests.get(telegram)
                     time.sleep(20)
        except Exception  as e:
            print("If this message pops up multiple times, please find the error and create a PR!")
            print (e)
            pass
        currentTime = datetime.datetime.now()
        print(currentTime.strftime("%Y-%m-%d %H:%M:%S") + "  No Slots found. Will retry again.")
        time.sleep(300)

def notify(title, text):
    if os.name == 'posix':
        os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
        os.system('say "Slots for delivery available!"')
    elif os.name == 'Linux':
        os.system('spd-say "Slots for delivery available!"')

def main():
    get_bb_slot('https://www.bigbasket.com/basket/?ver=1')

if __name__ == '__main__':
    main()
