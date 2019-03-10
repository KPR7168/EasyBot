from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import datetime
import uuid

phoneNumber = str(randint(10000000, 99999999))
driver = webdriver.Chrome(executable_path=r"./chromedriver")
driver.get("https://latest.staging.oneflare.com.au")

def clickXPath(xpath):
    driver.find_element_by_xpath(xpath).click()
    time.sleep(0.5)

def sendKeyXPath(key, xpath):
    element = driver.find_element_by_xpath(xpath)
    element.clear()
    element.send_keys(key)

def clickById(id):
    driver.find_element_by_id(id).click()
    time.sleep(0.5)

#click LOG IN
clickById('login-cta')

#click email login
clickById('login_with_email')

#type in email
sendKeyXPath("nak@bot.com", '//*[@id="user_email"]')

#type in password
sendKeyXPath("test1234", '//*[@id="user_password"]')

#click log in
clickById('login_btn')

#type in gardener
sendKeyXPath('Gardener', '//*[@id="gtm-my-jobs-request"]/span[1]/input')
time.sleep(0.5)
clickXPath('//*[@id="gtm-my-jobs-request"]/span[1]/span/div')

#type in postcode
sendKeyXPath('2000', '//*[@id="gtm-my-jobs-request"]/span[2]/input')
time.sleep(1)
clickXPath('//*[@id="gtm-my-jobs-request"]/span[2]/span/div')

#click continue
clickXPath('//*[@id="gtm-my-jobs-request"]/button')

#click garden maintenance
clickXPath('/html/body/div[4]/oui-request/div/div/form/oui-request-steps/oui-request-step[1]/div/section/div/label[1]')
#click next
clickXPath('/html/body/div[4]/oui-request/div/div/oui-request-nav/nav/a[1]')

#click wedding
clickXPath('/html/body/div[4]/oui-request/div/div/form/oui-request-steps/oui-request-step[2]/div/section/div/label[1]')
#click next
clickXPath('/html/body/div[4]/oui-request/div/div/oui-request-nav/nav/a[1]')

#click book regular service yes
clickXPath('/html/body/div[4]/oui-request/div/div/form/oui-request-steps/oui-request-step[22]/div/section/div/label[1]')
#click next
clickXPath('/html/body/div[4]/oui-request/div/div/oui-request-nav/nav/a[1]')

#click weekly
clickXPath('/html/body/div[4]/oui-request/div/div/form/oui-request-steps/oui-request-step[23]/div/section/div/label[1]')
#click next
clickXPath('/html/body/div[4]/oui-request/div/div/oui-request-nav/nav/a[1]')

#click lawn area
clickXPath('/html/body/div[4]/oui-request/div/div/form/oui-request-steps/oui-request-step[24]/div/section/div/label[1]')
#click next
clickXPath('/html/body/div[4]/oui-request/div/div/oui-request-nav/nav/a[1]')

#click as soon as pissble
clickXPath('/html/body/div[4]/oui-request/div/div/form/oui-request-steps/oui-request-step[26]/div/section/div/label[1]')
#click next
clickXPath('/html/body/div[4]/oui-request/div/div/oui-request-nav/nav/a[1]')

#type in further detail
sendKeyXPath('This lead was generated from NakBot.', '/html/body/div[4]/oui-request/div/div/form/oui-request-steps/oui-request-step[27]/div/section/div[1]/textarea')

#click request quotes
clickXPath('/html/body/div[4]/oui-request/div/div/oui-request-nav/nav/a[2]')

time.sleep(5)
driver.close()