from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as geckoService
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


def access_bot(url, uri):
    username = "*******"
    password = "*******"

    gecko_service = geckoService("/usr/local/bin/geckodriver")
    service = webdriver.FirefoxService(executable_path="/usr/local/bin/geckodriver")
    options = webdriver.FirefoxOptions()
       
    browser = webdriver.Firefox(options=options, service=service)
    options.add_argument("-headless")    
    browser.get(url)    
    time.sleep(2)
    try:   
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[1]/input').send_keys(username)      
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input').send_keys(password)
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[2]/input').send_keys(Keys.ENTER)
    except:
        browser.quit()
  
    time.sleep(2)
   
    code_url = browser.current_url
    browser.quit()  
    code = code_url.strip(f"{uri}?code=")
    
    return code