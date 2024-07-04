from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def realizar_automacao(cpf, pasta_destino):
    
    driver = webdriver.Chrome()
   
    
    try:
        # Abrir a página desejada
        url = 'https://esaj.tjsp.jus.br/cposg/open.do'
        driver.get(url)
        
        # Selecionar a opção correta no dropdown (exemplo genérico, ajuste conforme seu caso)
        # Aqui estamos clicando na terceira opção do dropdown
        dropdown = driver.find_element(By.XPATH, '/html/body/div[2]/form/section/div[1]/div/select')
        dropdown.find_element(By.XPATH, './option[3]').click()
    
        
        # Inserir o CPF no campo específico
        campo_cpf = driver.find_element(By.ID, 'campo_DOCPARTE')
        campo_cpf.send_keys(cpf)
        
        # Clicar no botão de pesquisa
        botao_pesquisar = driver.find_element(By.XPATH, '/html/body/div[2]/form/section/div[4]/div/input')
        botao_pesquisar.click()
        
        # Aguardar um momento para o carregamento da página e capturar screenshot
        time.sleep(2)  # Tempo de espera ajustável conforme necessário
        
        # Capturar o screenshot da página
        screenshot_path = os.path.join(pasta_destino, f'screenshot_{cpf}.png')
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot salvo em: {screenshot_path}')
        
    finally:
        # Fechar o navegador ao finalizar
        driver.quit()

# Exemplo de uso
if __name__ == '__main__':
    cpf = input('Digite o CPF (apenas números): ')  # Solicita o CPF ao usuário
    pasta_destino = 'C:\Users\escritório\Desktop\AUT\RESULTADO'  # Caminho da pasta onde deseja salvar os screenshots
    
    realizar_automacao(cpf, pasta_destino)
