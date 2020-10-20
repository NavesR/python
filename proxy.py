import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

proxy = '169.57.157.148:80'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get('https://www.myip.com/')
time.sleep(100)