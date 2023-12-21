
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