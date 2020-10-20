from selenium import webdriver
import time 

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get("https://discord.com/login?redirect_to=%2Fchannels%2F%40me")
driver.execute_script('function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 2500);}login("MzExMjkxODE0MDEzNDM1OTA2.X4ZZHA._IMFqNxqL8VOgg9ksimRFhHYGEI")')

time.sleep(4)


'''
driver2 = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver2.get("https://discord.com/login?redirect_to=%2Fchannels%2F%40me")
driver2.execute_script('function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 2500);}login("MzExMjkxODE0MDEzNDM1OTA2.X4ZZHA._IMFqNxqL8VOgg9ksimRFhHYGEI")')
'''