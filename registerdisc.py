from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get("https://discord.com/register")

#time.sleep(5)
email = driver.find_element_by_name('email').send_keys('eusouhelicopterosexual@gmail.com')
nome = driver.find_element_by_name('username').send_keys('Naves')
password = driver.find_element_by_name('password').send_keys('eusouhelicopterosexual@gmail.com')


#driver.execute_script('function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 2500);}login("MzExMjkxODE0MDEzNDM1OTA2.X4ZZHA._IMFqNxqL8VOgg9ksimRFhHYGEI")')


