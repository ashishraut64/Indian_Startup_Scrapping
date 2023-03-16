from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

Options=Options()
Options.add_experimental_option('detach', True)
s = Service('C:/Users/ASHISH SANJAY RAUT/Desktop/chromedriver_win32/chromedriver.exe')
driver =webdriver.Chrome(service=s, options=Options)
driver.get('https://www.failory.com/startups/india')
time.sleep(2)
driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
html=driver.page_source
with open('Startup.html','w',encoding='utf-8') as f:
    f.write(html)