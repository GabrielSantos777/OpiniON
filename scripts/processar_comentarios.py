import sqlite3
import json
import re

def limpar_texto(texto):
    """Remove caracteres especiais e espaços extras do comentário."""
    texto = re.sub(r'\s+', ' ', texto)  # Remove múltiplos espaços
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    return texto.strip()

def processar_comentarios():
    # Conectar ao banco de dados
    conn = sqlite3.connect("data/raw/comentarios_analise.db")
    cursor = conn.cursor()

    # Buscar os comentários do banco
    cursor.execute("SELECT comentario FROM comentarios")
    comentarios = cursor.fetchall()

    # Processar os comentários
    comentarios_limpos = list(set(limpar_texto(comentario[0]) for comentario in comentarios))  # Remove duplicatas

    # Salvar os comentários processados em JSON
    with open("data/processed/analise_sentimentos.json", "w", encoding="utf-8") as f:
        json.dump(comentarios_limpos, f, ensure_ascii=False, indent=4)

    print(f"Processamento concluído! {len(comentarios_limpos)} comentários salvos em 'data/raw/comentarios_processados.json'.")

    # Fechar conexão com o banco
    conn.close()

# Executar o processamento
if __name__ == "__main__":
    processar_comentarios()
