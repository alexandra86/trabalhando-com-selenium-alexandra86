from selenium import webdriver

from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

url = "http://selenium.dunossauro.live/aula_05_c.html"

chrome.get(url)


def melhor_filme(browser, filme, email, telefone):
    browser.find_element(By.NAME, "filme").send_keys(filme)
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "telefone").send_keys(telefone)
    browser.find_element(By.NAME, "enviar").click()


melhor_filme(chrome, "Os incríveis", "alexyamiranda7@gmail.com", "(21) 98996-4940")
