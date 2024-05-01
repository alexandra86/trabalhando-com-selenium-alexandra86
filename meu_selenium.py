from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

url = "http://selenium.dunossauro.live/aula_05_a.html"

chrome.get(url)

div_py = chrome.find_element(By.ID, "python")
div_hk = chrome.find_element(By.ID, "haskell")
print(div_hk.text)

chrome.quit()
