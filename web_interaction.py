import time
import os
from selenium import webdriver
user = ""
pwd = ""
driver = webdriver.Chrome('C:\Python34\webdrivers\chromedriver')
driver.get("https://login.naukri.com/nLogin/Login.php")
email = driver.find_element_by_id('emailTxt')
email.send_keys(user)
pasw = driver.find_element_by_id('pwd1')
pasw.send_keys(pwd)
time.sleep(5)
submitBtn = driver.find_element_by_name('Login')
submitBtn.click()
driver.get('https://my.naukri.com/Profile/view/subAction/ar?id=&altresid=#ar')
uploadLink = driver.find_element_by_id('uploadLink')
uploadLink.click()
attachCV = driver.find_element_by_id('attachCV')
attachCV.send_keys(os.path.abspath("SunilKumarK.doc"))
saveBtn = driver.find_elements_by_xpath('/html/body/div[4]/div[3]/div/form/div[7]/button')[0]
saveBtn.click()
