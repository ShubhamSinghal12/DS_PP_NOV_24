from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

url = "https://in.search.yahoo.com/"

driver.get(url)

element = driver.find_element(By.NAME, "p")
element.send_keys("Hello World"+Keys.RETURN)

time.sleep(3)
# element = driver.find_element(By.ID,'cols')
# print(element.get_attribute('outerHTML'))


elements = driver.find_elements(By.CSS_SELECTOR,'h3.title a')
for ele in elements:
    print(ele.text,ele.get_attribute('href'))



# element = driver.find_element(By.ID,'logo')
# element.click()
# time.sleep(3)

# driver.back()
# time.sleep(3)

# driver.forward()

time.sleep(5)
driver.quit()