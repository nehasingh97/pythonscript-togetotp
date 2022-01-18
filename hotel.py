from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.easemytrip.com/hotels/")
driver.implicitly_wait(5)
driver.maximize_window()
# driver.find_element_by_xpath("//*[@id="myTopnav"]/div[1]/ul/li[2]/a").click()
# driver.find_element_by_id("mainlogin").click()
time.sleep(3)
driver.find_element_by_id("txtCity").send_keys=("Delhi")
driver.find_element_by_id("txtCheckInDate").send_keys("21 July,2021")
driver.find_element_by_id("txtCheckOutDate").send_keys("22 July,2021")
print(driver.title)

