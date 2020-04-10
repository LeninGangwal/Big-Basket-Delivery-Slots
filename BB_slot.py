from selenium import webdriver
import chromedriver_autoinstaller
import sys
import time
import os


def get_bb_slot(url):
    # auto-install chromedriver 
    chromedriver_autoinstaller.install() 
    
    driver = webdriver.Chrome()
    driver.get(url)
    print("Please login using OTP and then wait for a while.")
    time.sleep(60)


    while 1:
        driver.get(url)     
        time.sleep(2)
        print("Trying to find a slot!")
        try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()
            time.sleep(3)  #driver take a few sec to update the new url
            if "checkout" in driver.current_url:
                print("Found the slots!")
                for i in range(60):
                     notify("Slots Available!", "Please go and choose the slots!")
                     time.sleep(20)
        except:
            print("If this message pops up multiple times, please find the error and create a PR!")
            pass
        print("No Slots found. Will retry again.")
        time.sleep(60)

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
