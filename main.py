# This is a sample Python script.
import urllib
import pyautogui as gui
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# ChromeOptions
# options = new
# ChromeOptions();
# options.addArguments("--headless");
# options.addArguments("--disable-gpu");
# options.addArguments("--disable-dev-shm-usage");
#
# URL
# url = new
# URL("http://localhost:4444/wd/hub");
# RemoteWebDriver
# driver = new
# RemoteWebDriver(url, options);
# driver.get("http://google.com");
# System.out.println(driver.getTitle());

options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.instagram.com/p/Cpb4WjIpVcb/")
# options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\BenotX\AppData\Local\Google\Chrome\User Data')
options.add_argument('--profile-directory=Default')
options.add_argument("--no-sandbox");
options.add_argument("--disable-dev-shm-usage");
# options.add_argument("--headless");
# options.add_argument("--disable-gpu");
# options.add_argument("--disable-dev-shm-usage");
# PATH = "/Users/yourPath/Desktop/chromedriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),executable_path=r'C:\Users\BenotX\Documents\chromedriver_win32\chromedriver', options=options)
driver.get("https://www.instagram.com/explore/")
time.sleep(5)
X,Y=gui.size()
print(X)
print(Y)
gui.moveTo(X/2,Y/2)
gui.click()
while True:

    try:
        time.sleep(15)  # during the 5 secs move your cursor to the website you want to scroll
        gui.press('Right')
        print(driver.current_url);
        # get the image source
        img = driver.find_element('//*[@id="mount_0_0_fw"]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]/div[1]/img')
        print(src);
        src = img.get_attribute('srcset')
        print(src);
        # urllib.urlretrieve(src)
        src = img.get_attribute('src')
        # filename = datetime.now().strftime('%Y%m%d%hh%mm%ss')
        # print(filename)
        print(src);
        # download the image
        # urllib.urlretrieve(src)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)