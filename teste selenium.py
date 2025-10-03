from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

# Acessa o site
driver.get("https://www.saucedemo.com/")
time.sleep(10)
# Faz login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(10)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(10)
driver.find_element(By.ID, "login-button").click()
time.sleep(10)
# Seleciona filtro "Price (low to high)"
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_value("lohi")

# Captura os preços
precos_elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
precos = [float(p.text.replace("$", "")) for p in precos_elementos]

# Verifica se está ordenado
if precos == sorted(precos):
    print("✅ Ordenação por preço (low to high) está correta!")
else:
    print("❌ Ordenação de preços incorreta!")

driver.quit()
