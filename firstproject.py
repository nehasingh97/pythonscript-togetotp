# import time
# from selenium import webdriver
# # Pass in the google chromedriver executable file save path.
# browser = webdriver.Chrome('../driver/chromedriver')
# browser.get('https://www.google.com') 
# time.sleep(50)

# browser.quit()
from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="./chromedriver")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.navjeevanbroking.com/rekyc")
#to refresh the browser
driver.refresh()
#to close the browser
# driver.close()
