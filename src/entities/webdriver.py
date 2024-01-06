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
    
    
    
    
    
    input_document = driver.find_element(By.XPATH, "//input[@id='campo_DOCPARTE']")
    dropdown_form = driver.find_element(By.XPATH, "//select[@id='cbPesquisa']")
    options_select = Select(dropdown_form)
    options_select.select_by_value('DOCPARTE')
    input_document.clear()
    input_document.send_keys(client_document)
    button_submit = driver.find_element(By.XPATH, "//input[@id='botaoConsultarProcessos']")
    button_submit.click()
    sleep(2)
    try:
        expand = driver.find_element(By.XPATH, "//a[@href='#maisDetalhes']")
        search(expand)
    except Exception as error:
        sg.popup_error('Não encontrou dados com o Documento informado.')
        valores['documento'] = ''
        janela['status'].update('')
        driver.close()
else:
    sg.popup_error('Digite algum documento!');
    janela['status'].update('')