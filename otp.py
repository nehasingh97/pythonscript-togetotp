from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="./chromedriver")
#MAXIMIZES THE WINDOW
driver.maximize_window()

#OPENS FLIPKART
driver.get("https://www.flipkart.com/")

#ENTERS MOBILE NUMBER ON WHICH 
#OTP IS TO BE SENT
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("7903000276")
#CLICKS ON FORGET PASSWORD 
#TO SEND THE FIRST OTP
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/a/span").click()

#RUNS THE LOOP 7 TIMES
for i in range (1,8):
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/a/span").click()
    #AFTER EVERY 1 SECOND OTP WOULD BE SENT
    time.sleep(1)
driver.close()