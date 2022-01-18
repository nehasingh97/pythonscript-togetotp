from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="./chromedriver")
#MAXIMIZES THE WINDOW
driver.maximize_window()

#OPENS FLIPKART
driver.get("https://www.navjeevanbroking.com/rekyc")
time.sleep(3)
#ENTERS MOBILE NUMBER ON WHICH 
#OTP IS TO BE SENT
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/input").send_keys("meon1")
time.sleep(8)
#CLICKS ON FORGET PASSWORD 
#TO SEND THE FIRST OTP
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/button").click()

#RUNS THE LOOP 7 TIMES
for i in range (1,8):
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div[4]/button[2]").click()
    #AFTER EVERY 1 SECOND OTP WOULD BE SENT
    time.sleep(60)
# driver.close()