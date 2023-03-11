# This is a sample Python script.
import urllib
from datetime import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver

from selenium.webdriver.common.keys import Keys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pyautogui as gui
import time


while True:
    time.sleep(5)  # during the 5 secs move your cursor to the website you want to scroll
    gui.press('Right')


    driver = webdriver.Chrome('./chromedriver')
    # get the image source
    img = driver.find_element_by_xpath('//*[@id="mount_0_0_fw"]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]/div[1]/img')
    src = img.get_attribute('srcset')
    filename = datetime.now().strftime('%Y%m%d%hh%mm%ss')
    print(filename)

    # download the image
    urllib.urlretrieve(src, filename)
    driver.current_url