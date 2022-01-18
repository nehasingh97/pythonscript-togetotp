from string import printable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.easemytrip.com/hotels/")
driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/div/div[5]/input").click()
time.sleep(20)
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
driver.close()