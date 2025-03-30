import json
import google.generativeai as genai
import time
import os

# 🔒 Carregar a API Key de uma variável de ambiente (MELHOR SEGURANÇA)
API_KEY = os.getenv("GOOGLE_API_KEY")  # Defina isso no seu ambiente
if not API_KEY:
    raise ValueError("⚠️ API Key não encontrada! Defina a variável de ambiente GOOGLE_API_KEY.")

genai.configure(api_key=API_KEY)

# Configurar o modelo uma vez (EVITA RECRIAÇÃO DESNECESSÁRIA)
modelo = genai.GenerativeModel("gemini-pro")


def analisar_sentimento_lote(textos):
    """
    Envia múltiplos comentários em uma única chamada para reduzir consumo da API.
    """
    prompt = "\n".join([f"{i+1}. {texto}" for i, texto in enumerate(textos)])
    prompt = f"Classifique os seguintes comentários como Positivo, Neutro ou Negativo:\n{prompt}"

    for tentativa in range(3):  # Tenta até 3 vezes em caso de erro
        try:
            resposta = modelo.generate_content(prompt)
            return resposta.text.strip().split("\n")  # Retorna lista de sentimentos
        except Exception as e:
            print(f"⚠️ Erro na análise (tentativa {tentativa + 1}/3): {e}")
            time.sleep(10)  # Espera antes de tentar novamente

    return ["Erro"] * len(textos)  # Retorna "Erro" para todos os comentários se falhar


def analisar_sentimentos():
    # Carregar os comentários processados
    with open("data/raw/comentarios.json", "r", encoding="utf-8") as f:
        comentarios = json.load(f)

    resultados = []

    # Processa em LOTES de 5 comentários (EVITA ESTOURAR COTA)
    tamanho_lote = 5
    for i in range(0, len(comentarios), tamanho_lote):
        lote = comentarios[i : i + tamanho_lote]
        sentimentos = analisar_sentimento_lote(lote)

        for comentario, sentimento in zip(lote, sentimentos):
            resultados.append({"comentario": comentario, "sentimento": sentimento})


    # Salvar os resultados em um JSON
    with open("data/processed/analise_sentimentos.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    analisar_sentimentos()







