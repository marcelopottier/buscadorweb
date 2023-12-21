from src.entities.proccess import Proccess

def getDataFromWeb(driver):
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
    
    return Proccess(processoId, processoClasse, processoAssunto, processoForo, processoVara, processoJuiz, processoDistribuicao, processoControle, processoArea, processoValor,
                  partesProcesso, arrDataMovimentacoes, arrDescricaoMovimentacoes)

