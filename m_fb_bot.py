from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from sentence import dic

sentence = dic["sentence"]
image = dic["image"]
image = image[2:-2]

#print(sentence, image)

username = 'your email goes here'
password = 'your password goes here'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications" : 2})
driver = webdriver.Chrome("C:\Python\chromedriver.exe", options=chrome_options)
driver.get('https://m.facebook.com/')

#####logging in

driver.find_element_by_id('m_login_email').send_keys(username)
driver.find_element_by_id('m_login_password').send_keys(password)
driver.find_element_by_id('u_0_4').click()
time.sleep(3)
driver.find_element_by_css_selector("button[value='OK']").click()

#####posting

time.sleep(3)
#driver.get('') #if you don't want to post on your wall: uncomment and insert the link to a page you manage
time.sleep(3)
driver.find_element_by_css_selector("a[aria-label='Publish']").click()
time.sleep(3)
driver.find_element_by_id('u_0_2s').send_keys(image) 
time.sleep(2)
driver.find_element_by_id('u_0_2s').clear()
time.sleep(2)
driver.find_element_by_id('u_0_2s').send_keys(sentence) 
time.sleep(2)
driver.find_element_by_css_selector("button[value='Post'][data-sigil='touchable submit_composer']").click()
time.sleep(2)
alert_obj = driver.switch_to.alert
alert_obj.accept()

#driver.quit() #uncomment to close the browser automatically