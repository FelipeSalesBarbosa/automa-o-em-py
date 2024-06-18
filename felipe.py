from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def realizar_automacao(cpf, pasta_destino):
  

    driver = webdriver.Chrome()
   
    
    try:
        url = 'https://esaj.tjsp.jus.br/cpopg/open.do'
        driver.get(url)
        
        
        dropdown = driver.find_element(By.XPATH, '/html/body/div[2]/form/section/div[1]/div/select')
        dropdown.find_element(By.XPATH, './option[3]').click()
    
         
       
        campo_cpf = driver.find_element(By.ID, 'campo_DOCPARTE')
        campo_cpf.send_keys(cpf)
        
        
        botao_pesquisar = driver.find_element(By.XPATH, '/html/body/div[2]/form/section/div[4]/div/input')
        botao_pesquisar.click()
        
        
        time.sleep(2)  
        
        
        screenshot_path = os.path.join(pasta_destino, f'screenshot_{cpf}.png')
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot salvo em: {screenshot_path}')
        
    finally:
        
        driver.quit()


if __name__ == '__main__':
    cpf = input('Digite o CPF (apenas números): ')  
    pasta_destino = 'C:\\Users\\escritório\\Desktop\\AUT'  
    
    realizar_automacao(cpf, pasta_destino)


