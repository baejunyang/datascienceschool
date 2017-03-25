# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd
from comments_dao import Dao

#chromedriver = './chromedriver'
driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.ssodam.com/')
wait = WebDriverWait(driver,10)

try:
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-dismiss='modal']")))
    button.click()
except:
    pass

button2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-target='#loginModal']")))
time.sleep(1)
button2.click()

email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class='form-control']")))
email.clear()
email.send_keys('enjoi')

password = driver.find_element_by_css_selector("input[placeholder='Password']")
password.clear()
password.send_keys('ame306')

login = driver.find_element_by_css_selector("input[class='submit btn btn-default']")
login.click()

time.sleep(1)

alert = driver.switch_to_alert()
alert.accept()

start = 193294; end = 193300
comments_dict = OrderedDict()
comments_dict['text'] = []
comments_dict['date'] = []

for i in range(start, end):
    driver.get('http://www.ssodam.com/content/{}'.format(i))
    try:
        comment_num = driver.find_element_by_xpath("//div[@class='comment-number']")
    except:
        continue

    if comment_num.text == u'댓글 0개':
        continue

    div = driver.find_element_by_xpath("//div[@id='comments_area_html']")
    div2 = div.find_elements_by_xpath("//div[@class='mverdana comment-content']")
    div3 = div.find_elements_by_xpath("//div[@class='comment-date']")
    div4 = div.find_elements_by_xpath("//div[@class='mverdana comment-content comment-user-writer']")

    for comments in div2 :
        comments_dict['text'].append(comments.text.encode('utf-8'))
        print comments.text.encode('utf-8')

    for comments in div4 :
        comments_dict['text'].append(comments.text.encode('utf-8'))

    for date0 in div3 :
        if not date0.get_attribute('style') :
            date = '2017' + '-' + re.sub(r'/', '-', date0.text)
            comments_dict['date'].append(date)
comments_dao = Dao(comments_dict)
commnts_dao.session_add()
driver.quit()
display.stop()

#df = pd.DataFrame(comments_dict)
#df.to_csv('./files/crawl_reply{}_{}.csv'.format(start,end))
#df
