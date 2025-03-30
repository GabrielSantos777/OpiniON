import json
import matplotlib.pyplot as plt
import re

def exibir_grafico():
    # Nome do arquivo JSON com a análise de sentimentos
    arquivo_json = "data/processed/analise_sentimentos.json"

    # Carregar os dados do arquivo JSON
    try:
        with open(arquivo_json, "r", encoding="utf-8") as f:
            dados = json.load(f)  # Supondo que o JSON seja uma lista de dicionários
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_json} não foi encontrado.")
        exit()

    # Contar a quantidade de cada sentimento
    contagem_sentimentos = {"Positivo": 0, "Neutro": 0, "Negativo": 0}

    for comentario in dados:
        sentimento_bruto = comentario.get("sentimento", "").strip()
        
        # Remover números, asteriscos e caracteres especiais, mantendo apenas "Positivo", "Neutro" ou "Negativo"
        sentimento_limpo = re.sub(r"[^a-zA-Z]", " ", sentimento_bruto).strip()

        # Se o sentimento estiver na contagem, incrementar
        if sentimento_limpo in contagem_sentimentos:
            contagem_sentimentos[sentimento_limpo] += 1

    # Dados para o gráfico
    sentimentos = list(contagem_sentimentos.keys())
    quantidades = list(contagem_sentimentos.values())

    # Definir cores para cada sentimento
    cores = {"Positivo": "green", "Neutro": "gray", "Negativo": "red"}
    cores_barras = [cores[sent] for sent in sentimentos]

    # Criar gráfico de barras
    plt.figure(figsize=(6, 4))
    plt.bar(sentimentos, quantidades, color=cores_barras)

    # Configurar rótulos
    plt.xlabel("Sentimento")
    plt.ylabel("Quantidade de Comentários")
    plt.title("Análise de Sentimentos dos Comentários")

    # Ajustar limites para melhor visualização
    plt.ylim(0, max(quantidades) * 1.2 if max(quantidades) > 0 else 1)

    # Mostrar os valores em cima das barras
    total = sum(quantidades)
    for i, v in enumerate(quantidades):
        if total > 0:
            porcentagem = (v / total) * 100
            plt.text(i, v + 0.1, f"{v} ({porcentagem:.1f}%)", ha='center', fontsize=12, fontweight='bold')

    # Exibir gráfico
    plt.show()

# Chamar a função para exibir o gráfico
exibir_grafico()
