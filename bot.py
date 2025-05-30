from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as geckoService
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


def access_bot(url, uri):    
    service = webdriver.FirefoxService(executable_path="/usr/local/bin/geckodriver")
    options = webdriver.FirefoxOptions()    
    profile = webdriver.FirefoxProfile("**********")
    profile.set_preference("javascript.enabled", False)
    options.profile = profile
           
    browser = webdriver.Firefox(options=options, service=service)
    time.sleep(2)    
    try:
        browser.get(url)
    except:
        code_url = browser.current_url
        browser.quit()  
        code = code_url.strip("https://127.0.0.1:8888/callback?code=")        
   
    return code