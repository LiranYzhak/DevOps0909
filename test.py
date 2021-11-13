from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# my_driver = webdriver.Chrome(executable_path="/Users/apple/Downloads/chromedriver")
# my_driver.get("https://translate.google.com/")
# my_driver.find_element_by_id("text_area").send_keys("שלום")
# my_driver.find_element_by_id("gt-submit").click()

from selenium.webdriver.chrome.service import Service
# chrome = Service("/Users/apple/Downloads/chromedriver")
# driver = webdriver.Chrome(service=chrome)
driver = webdriver.Firefox(executable_path="/Users/apple/Downloads/geckodriver")
driver.get("https://www.youtube.com/")
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("beatles")
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()

