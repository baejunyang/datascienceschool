import time
import pandas as pd
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800,600))
display.stary()

chromedriver = './files/chromedriver'
driver = webdriver.Chrome(chromedriver)
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

crawl = OrderedDict()
crawl['title'] = []
crawl['body'] = []
crawl['date'] = []

comments_dict = OrderedDict()
comments_dict['text'] = []

start = 223249; stop=233249
for i in range(start, stop):
    driver.get('http://www.ssodam.com/content/{}'.format(i))
    try:
        title = driver.find_element_by_xpath("//div[@class='board-title']")
        body = driver.find_element_by_xpath("//div[@class='board-content mverdana']")
        date = driver.find_element_by_xpath("//div[@class='board-date row col-lg-3 col-xs-12 desktop-hide']")
    except:
        continue

    try:
        crawl['title'].append(title.text.encode('utf-8'))
        crawl['body'].append(body.text.encode('utf-8'))
        crawl['date'].append(date.text.encode('utf-8'))
    except :
        continue

    comment_num = driver.find_element_by_xpath("//div[@class='comment-number']")
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



driver.quit()
display.stop

df_crawl = pd.DataFrame(crawl)
df_comments = pd.DataFrame(comments_dict)
df_crawl.to_csv('crawl{}_{}.csv'.format(start, stop))
df_comments.to_csv('comments{}_{}.csv'.format(start,stop))
