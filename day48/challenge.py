from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#keep chrome browser open after programe finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

firstname = driver.find_element(By.NAME, value="fName")
firstname.send_keys("Ritesh")
lastname = driver.find_element(By.NAME, value="lName")
lastname.send_keys("Patil")
email = driver.find_element(By.NAME, value="email")
email.send_keys("patilritesh4016@gmail.com")

sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up_button.click()



# driver.close()
