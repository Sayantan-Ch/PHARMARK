from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
meds=[]
meds.append(input())
driver = webdriver.Firefox()
driver.get('https://ipindiaonline.gov.in/tmrpublicsearch/frmmain.aspx')
wait = WebDriverWait(driver, 10)
# time.sleep(1)
# driver.implicitly_wait(10)
wordmarkelem = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_TBWordmark")
classelem = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_TBClass")
searchelem = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_BtnSearch")
wordmarkelem.send_keys(meds[0])
classelem.send_keys("5")
searchelem.click()
# count = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_LblSearchDetail > table:nth-child(1) > tbody:nth-child(1) > td:nth-child(1)").text
count = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ContentPlaceHolder1_LblSearchDetail > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1)"))).text

count = count.split(' ')[-1]
print(count)
if int(count) == 0:
    meds.pop()
print(meds)
driver.close()
