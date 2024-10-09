from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome browser open after programe finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

title = driver.find_element(By.CLASS_NAME, "menu")
print(title.text)

driver.maximize_window()

driver.close()
# driver.quit()