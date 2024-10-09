from selenium import webdriver
from selenium.webdriver.common.by import By

#keep chrome browser open after programe finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
total_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(total_articles.text)
# total_articles.click() #click

search = driver.find_element(By.CSS_SELECTOR, value="#searchform")
search.send_keys("Python")

driver.close()