from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CustomWebDriver:
    def __init__(self, options=None, service=None):        
        self.options = options or Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-dev-shm-usage')
        self.service = service or Service(ChromeDriverManager().install())   
        self.driver = webdriver.Chrome(options=self.options, service=self.service)

    def close(self):     
        self.driver.quit()
    
    def get(self, url):
        self.driver.get(url)