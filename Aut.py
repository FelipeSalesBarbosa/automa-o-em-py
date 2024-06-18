from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

# Função para realizar a automação
def realizar_automacao(cpf, url, pasta_destino):
    # Configuração do WebDriver
    driver = webdriver.Chrome
    
    try:
        # Abrir o navegador e acessar o site desejado
        driver.get()
        
        # Localizar o campo de CPF e inserir o CPF fornecido
        
        driver.find_element_by_xpath('/html/body/div[2]/form/section/div[1]/div/select/option[3]').click()
        campo_cpf = driver.find_element_by_xpath('/html/body/div[2]/form/section/div[2]/div/div[3]/div[1]/input')  # Substitua pelo ID do campo de CPF no seu site
        campo_cpf.send_keys(cpf)
        
        # Submeter o formulário (se necessário)
        
        # Aguardar o carregamento da página (pode ser ajustado conforme necessário)
        time.sleep(2)
        
        # Capturar o screenshot da página
        screenshot_path = os.path.join(pasta_destino, f'screenshot_{cpf}.png')
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot salvo em: {screenshot_path}')
        
    finally:
        # Fechar o navegador ao finalizar
        driver.quit()

# Exemplo de uso
if __name__ == '__main__':
    cpf = '46966700827'  # Substitua pelo CPF desejado
    url = 'https://esaj.tjsp.jus.br/cpopg/open.do'  # Substitua pela URL do site
    pasta_destino = '/AUT'  # Substitua pelo caminho da pasta onde deseja salvar os screenshots
    
    realizar_automacao(cpf, url, pasta_destino)
