from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do navegador
chrome_options = Options()
chrome_options.add_argument("--headless")  # Rodar em segundo plano
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL do produto (substitua pela URL correta)
url = "https://www.amazon.com.br/Barra-Prote%C3%ADna-BOLD-Snacks-Mista/dp/B0D482P21J?ref=dlx_deals_dg_dcl_B0D482P21J_dt_sl14_e2_pi&pf_rd_r=G7XGVCAQ6FYV1BJTAV80&pf_rd_p=69cbcfa0-fee4-4854-af86-baaef099b7e2"
driver.get(url)

# Esperar a página carregar
time.sleep(5)

# Rolando até a seção de avaliações
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(3)

# Tentar encontrar os comentários
try:
    comments = driver.find_elements(By.CLASS_NAME, "review-text-content")
    reviews = [comment.text.strip() for comment in comments if comment.text.strip()]
    
    if reviews:
        print("Comentários encontrados:")
        print(reviews)
    else:
        print("Nenhum comentário encontrado. Tente inspecionar a página e ajustar a classe CSS.")
except Exception as e:
    print("Erro ao capturar comentários:", e)

# Fechar o navegador
driver.quit()

