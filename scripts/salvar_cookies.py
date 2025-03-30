import json
import time
from selenium import webdriver

# Iniciar o driver
driver = webdriver.Chrome()
driver.get("https://www.amazon.com.br")

# Aguarde tempo para login manual
print("Faça login manualmente na Amazon e aguarde...")
time.sleep(40)  # Tempo para você logar

# Capturar cookies e salvar
cookies = driver.get_cookies()

with open("cookies_amazon.json", "w", encoding="utf-8") as file:
    json.dump(cookies, file, indent=4)

print("Cookies salvos com sucesso!")
driver.quit()
