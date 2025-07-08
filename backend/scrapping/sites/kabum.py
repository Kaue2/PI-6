from scrapping.utils.browser import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def scrap_kabum(term: str = ""):
    driver = get_driver(headless=False)
    
    search_url = f"https://www.kabum.com.br/{term}"
    driver.get(search_url)
    
    # aguardando os produtos serem carregados
    try: 
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "productCard"))
        ) 
    except:
        print("Erro ao carregar os produtos")
        driver.quit()
        return []
    
    products = driver.find_elements(By.CLASS_NAME, "productCard")
    
    result = []
    
    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "nameCard").text
            price = product.find_element(By.CLASS_NAME, "priceCard").text
            result.append({"name": name, "price": price})
        except Exception:
            print("Erro ao salvar o produto: ", Exception)
    
    driver.quit()
    return result
        