from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
sumary: Cria e configura um chrome webdriver
params: headless, define se o navegador deve ter interface gráfica ou não
caso True, o navegador NÃO abrirá a interface gráfica
return: retorna uma instância do chrome web driver
"""
def get_driver(headless: bool = True):
    options = webdriver.ChromeOptions()
    
    # configura o navegador, como extensões, modo de exibição, etc
    if headless: 
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
    options.add_argument("--disable-dev-shm-usage") 
    
    # instala uma versão do webdriver compatível com o OS e passa as configurações anteriormente definidas
    driver = webdriver.Chrome( 
        service=Service(ChromeDriverManager().install()), 
        options=options)
    
    return driver