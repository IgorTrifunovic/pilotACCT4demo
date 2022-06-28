import time
from selenium import webdriver
driver = webdriver.Chrome('/home/igor/acct_automate/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver') # typing in serach box
search_box.submit() # serach query
time.sleep(5) # Let the user actually see something!

driver.quit() # quit and close

