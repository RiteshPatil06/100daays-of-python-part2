from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#keep chrome browser open after programe finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = {
    "https://www.linkedin.com/jobs/search/?currentJobId=4045387342&f_AL=true&f_TPR=r2592000&geoId=90009642&keywords=python%20developer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&sortBy=R"
}

driver = webdriver.Chrome(options=chrome_options)
driver.get(url= url)

