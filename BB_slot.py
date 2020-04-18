from selenium import webdriver
import chromedriver_autoinstaller
from plyer import notification
import sys
import time
import os

def printTime(msg=""):
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[{}]:{}".format(current_time,msg), end="\n")

def windows10Notifier(title="", msg=""):
    from plyer import notification

    notification.notify(
        title=title,
        message=msg,
        app_name='Big Basket Delivery Slot Notifier'
    )

def get_bb_slot(url):
    print()
    printTime("Do this on chromeTab:")
    printTime("1) Please LOGIN using OTP using mobile or emailID in newly opened chrome window")
    printTime("2) Choose correct delivery location on web page.")
    printTime("3) Wait on the basket's page and keep it open")  
    print()
    printTime("IMPORTANT: Keep browser tab open and this command window running")
    printTime("Wish you happy and safe stay #GO_CORONA")

    time.sleep(5) #added wait to load above msgs
    chromedriver_autoinstaller.install() 
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(60)
    
    tryCount = 1
    while 1:
        driver.get(url)     
        time.sleep(2)
        printTime("Trycount#{} Finding a slot!".format(tryCount))
        try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()

            time.sleep(5)  #driver take a few sec to update the new url
            src = driver.page_source
            if "checkout" in driver.current_url and not "Unfortunately, we do not have" in src:
                printTime("Found the slots!")
                for i in range(60):
                     notify("Big Basket Delivery Slots Available!", "Please go and choose the slots!")
                     time.sleep(20)
                     print("Ctrl+c this program once you are done with checkout and payment.")
        except Exception  as e:
            printTime("Please stay on basket's page.")
            printTime("If this message pops up multiple times, please find the error and create a PR!")
            print(e)
            pass
        printTime("No Slots found, will retry in a minute.")
        tryCount = tryCount+1
        time.sleep(60)

def notify(title, text):
    if os.name == 'nt':
        windows10Notifier(title, text)
    elif os.name == 'posix':
        os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
        os.system('say "Slots for delivery available!"')
    elif os.name == 'Linux':
        os.system('spd-say "Slots for delivery available!"')

def main():
    printTime("Prerequisite: You have items added to your bigbasket and correct delivery address")
    get_bb_slot('https://www.bigbasket.com/basket/?ver=1')

if __name__ == '__main__':
    main()
