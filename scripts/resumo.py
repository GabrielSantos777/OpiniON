import json
import re

def exibir_resumo():

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

    # Total de comentários
    total_comentarios = sum(contagem_sentimentos.values())

    # Calcular porcentagens
    if total_comentarios > 0:
        porcentagens = {
            "Positivo": (contagem_sentimentos["Positivo"] / total_comentarios) * 100,
            "Neutro": (contagem_sentimentos["Neutro"] / total_comentarios) * 100,
            "Negativo": (contagem_sentimentos["Negativo"] / total_comentarios) * 100,
        }
    else:
        print("Nenhum comentário disponível para análise.")
        exit()

    # Criar um resumo com base nos dados
    resumo = "🔍 **Resumo da Análise:**\n"
    resumo += f"- Comentários Positivos: {contagem_sentimentos['Positivo']} ({porcentagens['Positivo']:.1f}%)\n"
    resumo += f"- Comentários Neutros: {contagem_sentimentos['Neutro']} ({porcentagens['Neutro']:.1f}%)\n"
    resumo += f"- Comentários Negativos: {contagem_sentimentos['Negativo']} ({porcentagens['Negativo']:.1f}%)\n\n"

    # Definir recomendação com base nos dados
    if porcentagens["Positivo"] > 60:
        recomendacao = "✅ A maioria das avaliações são positivas! O produto parece ser uma boa escolha. Vale a pena considerar a compra."
    elif porcentagens["Negativo"] > 40:
        recomendacao = "❌ Muitos clientes tiveram experiências negativas. Talvez seja melhor pesquisar alternativas antes de comprar."
    else:
        recomendacao = "⚖️ Há opiniões mistas sobre o produto. Pode ser uma boa compra, mas vale a pena analisar os comentários detalhadamente."

    # Exibir resultado
    print(resumo)
    print(recomendacao)
