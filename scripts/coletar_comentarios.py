import json
import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def salvar_no_banco(produto, comentarios):
    """Salva os comentários no banco de dados SQLite."""
    conn = sqlite3.connect("data/raw/comentarios_analise.db")
    cursor = conn.cursor()

    for comentario in comentarios:
        cursor.execute("INSERT INTO comentarios (produto, comentario) VALUES (?, ?)", (produto, comentario))

    conn.commit()
    conn.close()
    print(f"✅ {len(comentarios)} comentários salvos no banco!")

def coletar_e_salvar():
    """Coleta os comentários da Amazon e armazena no banco de dados."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.amazon.com.br")

    # Carregar cookies salvos para login automático
    try:
        with open("cookies_amazon.json", "r", encoding="utf-8") as file:
            cookies = json.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()
        time.sleep(5)
        print("✅ Login automático bem-sucedido!")
    except FileNotFoundError:
        print("❌ Erro: Arquivo de cookies não encontrado. Execute salvar_cookies.py primeiro.")
        driver.quit()
        return

    # URL do produto
    url_produto = "https://www.amazon.com.br/dp/6589820198/"
    driver.get(url_produto)
    time.sleep(5)

    # Nome do Produto
    try:
        nome_produto = driver.find_element(By.ID, "productTitle").text.strip()
        print(f"📌 Produto encontrado: {nome_produto}")
    except NoSuchElementException:
        nome_produto = "Desconhecido"
        print("⚠️ Nome do produto não encontrado!")

    # Tentar abrir página de avaliações
    try:
        botao_veja_mais = driver.find_element(By.XPATH, "//a[contains(text(), 'Veja mais avaliações')]")
        driver.execute_script("arguments[0].click();", botao_veja_mais)
        time.sleep(5)
        print("✅ Página de avaliações aberta com sucesso!")
    except NoSuchElementException:
        print("⚠️ Botão 'Veja mais avaliações' não encontrado. Indo direto para os comentários...")

    comentarios = []
    pagina = 1

    while True:
        print(f"📌 Coletando comentários da página {pagina}...")

        # Capturar os comentários
        elementos = driver.find_elements(By.XPATH, "//span[@data-hook='review-body']")
        for elemento in elementos:
            comentarios.append(elemento.text.strip())

        print(f"📊 Total de comentários coletados até agora: {len(comentarios)}")

        # Tentar avançar para a próxima página de avaliações
        try:
            proximo_botao = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
            driver.execute_script("arguments[0].click();", proximo_botao)
            time.sleep(5)
            pagina += 1
        except NoSuchElementException:
            print("🚀 Não há mais páginas para carregar.")
            break
        except TimeoutException:
            print("⚠️ Erro ao carregar a próxima página.")
            break

    # Salvar os comentários no banco de dados
    salvar_no_banco(nome_produto, comentarios)

    driver.quit()
    print(f"✅ Coleta finalizada. Total de comentários coletados: {len(comentarios)}")

if __name__ == "__main__":
    coletar_e_salvar()
