from selenium import webdriver


#1a.
from selenium.webdriver.chrome.service import Service
chrome = Service("/Users/apple/Downloads/chromedriver")
my_driver_chrome = webdriver.Chrome(service=chrome)
my_driver_chrome.get("http://www.walla.co.il")
#2.
my_driver_chrome.refresh()
my_title = "וואלה! - האתר המוביל בישראל - עדכונים מסביב לשעון"
get_title = my_driver_chrome.title
if get_title == my_title:
    print("equal")
else:
    print("not equal")
my_driver_chrome.quit()

#1.b
my_driver_firefox = webdriver.Firefox(executable_path="/Users/apple/Downloads/geckodriver")
my_driver_firefox.get("http://www.ynet.co.il")
my_driver_firefox.quit()

#3 Same elements different browser

#4
my_driver = webdriver.Chrome(executable_path="https://translate.google.com/")
