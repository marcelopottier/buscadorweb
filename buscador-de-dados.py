from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import openpyxl


def search(expand):
    expand.click()
    processoId = driver.find_element(By.XPATH, "//span[@id='numeroProcesso']").text
    processoClasse = driver.find_element(By.XPATH, "//span[@id='classeProcesso']").text
    processoAssunto = driver.find_element(By.XPATH, "//span[@id='assuntoProcesso']").text
    processoForo = driver.find_element(By.XPATH, "//span[@id='foroProcesso']").text
    processoVara = driver.find_element(By.XPATH, "//span[@id='varaProcesso']").text
    processoJuiz = driver.find_element(By.XPATH, "//span[@id='juizProcesso']").text
    processoDistribuicao = driver.find_element(By.XPATH, "//div[@id='dataHoraDistribuicaoProcesso']").text
    processoControle = driver.find_element(By.XPATH, "//div[@id='numeroControleProcesso']").text
    processoArea = driver.find_element(By.XPATH, "//div[@id='areaProcesso']").text
    processoValor = driver.find_element(By.XPATH, "//div[@id='valorAcaoProcesso']").text
    partesProcesso = driver.find_elements(By.XPATH, "//td[@class='nomeParteEAdvogado']")
    arrPartesProcesso = [partes.text for partes in partesProcesso]

    #movimentações
    dataMovimentacoes = driver.find_elements(By.XPATH, "//tr[contains(@class, 'containerMovimentacao')]//td[contains(@class, 'dataMovimentacao')]")
    descricaoMovimentacoes = driver.find_elements(By.XPATH, "//tr[contains(@class, 'containerMovimentacao')]//td[contains(@class, 'descricaoMovimentacao')]")
    arrDataMovimentacoes = [data.text for data in dataMovimentacoes[:4]]
    arrDescricaoMovimentacoes = [descricao.text for descricao in descricaoMovimentacoes[:4]]

    driver.close()

while True:

    if eventos == 'Pesquisar':
        janela['status'].update('Buscando Dados...')
        if valores['documento'] != '':
            driver.get('https://esaj.tjsp.jus.br/cpopg/open.do')
            client_document = valores['documento']
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