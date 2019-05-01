from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import datetime
import uuid

phoneNumber = str(randint(10000000, 99999999))
driver = webdriver.Chrome(executable_path=r"./chromedriver")
driver.get("https://beta.urbanyou.com.au")

def clickXPath(xpath):
    driver.find_element_by_xpath(xpath).click()
    time.sleep(0.5)

def sendKeyXPath(key, xpath):
    element = driver.find_element_by_xpath(xpath)
    element.clear()
    element.send_keys(key)

#select book now
driver.find_element_by_id('btn-book-now-header').click()
time.sleep(0.5)

#select cleaning
clickXPath('//*[@id="cleaning-button"]')

#select end of least
clickXPath('//*[@id="eol-cleaning-button"]')
time.sleep(1)

#type in postcode
postcode = driver.find_element_by_id('cart_postcode')
postcode.clear()
postcode.send_keys('2000')

#type in email
email = driver.find_element_by_id('cart_email')
email.clear()
email.send_keys(phoneNumber+"@nakbot.com")
time.sleep(0.5)

#select GET PRICE
clickXPath('//*[@id="cart"]/div/div/div[6]/div/button')

#select NEXT
clickXPath('//*[@id="booking"]/div/div[1]/div[2]/div/form/div[5]/div/button')

#toggle calendar
time.sleep(0.5)
clickXPath('//*[@id="start_at"]')

#select tomorrow date
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
calendar = driver.find_element_by_xpath('//*[@id="booking"]/div/div[1]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div')
calendarSpan = calendar.find_elements_by_xpath('//span')
tomorrowSpan = filter(lambda x: x.text == str(tomorrow.day), calendarSpan)[0]
index = str(calendarSpan.index(tomorrowSpan) - 13) #13 is any span before 1st date
clickXPath('//*[@id="booking"]/div/div[1]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/span['+index+']')

#select start time
clickXPath('//*[@id="start_time"]/option[4]')

#type in address
address = driver.find_element_by_xpath('//*[@id="property_address"]')
address.send_keys('120 Sussex Street, SYDNEY NSW 2000')

#select try the full form
time.sleep(2)
clickXPath('//*[@id="booking"]/div/div[1]/div[2]/div/form/div[1]/div/div[3]/div[1]/div[1]/div/small[3]/span/a')

#fill in suburb
sendKeyXPath('Sydney', '//*[@id="property_suburb"]')

#fill in state
sendKeyXPath('NSW', '//*[@id="property_state"]')

#select property access
clickXPath('//*[@id="access-row"]/div[1]/div/div/div[1]/label')

#type in access instruction
sendKeyXPath('I dont know what to put in access instruction so here is random text just for testing.', '//*[@id="access_notes"]')

#click NEXT
clickXPath('//*[@id="booking"]/div/div[1]/div[2]/div/form/div[2]/div/button')
time.sleep(1)

#fill in client detail
sendKeyXPath('Nak', '//*[@id="cart_first_name"]')
sendKeyXPath('Bot', '//*[@id="cart_last_name"]')
sendKeyXPath('04'+phoneNumber, '//*[@id="cart_phone"]')
sendKeyXPath(str(uuid.uuid4().hex), '//*[@id="cart_password"]')

#select T&C
clickXPath('//*[@id="booking"]/div/div[1]/div[2]/div/form/div[1]/div/div[3]/div/div/div/label/span[1]')

#select BOOK & PAY
clickXPath('//*[@id="booking"]/div/div[1]/div[2]/div/form/div[2]/div/button')
time.sleep(7)

#fill in credit card
driver.switch_to_frame(frame_reference=driver.find_element_by_xpath('//iframe[@name="stripe_checkout_app"]'))
card = driver.find_element_by_xpath('//input[@placeholder="Card number"]')
card.send_keys('4242424242424242')

cardDate = driver.find_element_by_xpath('//input[@placeholder="MM / YY"]')
cardDate.send_keys('1221')

cardCVC = driver.find_element_by_xpath('//input[@placeholder="CVC"]')
cardCVC.send_keys('168')

#select pay button
clickXPath('//*[@id="container"]/section/span[2]/div/div/main/form/nav/div/div/div/button')

time.sleep(20)
driver.close()
print('Successfully create new booking in UrbanYou!')