from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import json



datos = open("./credenciales.txt", "rt", encoding = 'utf-8')
credenciales = datos.readlines()
driver = webdriver.Edge()
driver.get('https://www.url.edu.gt/login/')
time.sleep(2)

element = driver.find_element(By.XPATH, '//*[@id="Username"]')
element.send_keys(credenciales[0].strip())
element = driver.find_element(By.XPATH, '//*[@id="Password"]')
element.send_keys(credenciales[1])
time.sleep(1)

element = driver.find_element(By.XPATH, '//*[@id="Button1"]').click()
time.sleep(5)