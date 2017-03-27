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
