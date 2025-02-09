from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Inicializar o analisador
analyzer = SentimentIntensityAnalyzer()

# Lista de comentários já limpos
comentarios_limpos = [
    "muito gostoso vale o investimento muito bom minha nutricionista recomenda",
    "muito bom e com a possibilidade de experimentar diferentes sabores",
    "melhor barrinha pena que é tão cara só dá p comprar na promo",
    "essa barrinha é uma delícia e realmente satisfaz pela quantidade de proteína compro direto e amo",
    "realmente tem sabores muito bons para uma barra de proteina mas tem outros que nem tanto a barrinha é boa mas é mt cara vale a experiência",
    "produto bom chegou no prazo estimado veio bem embalado e são muitas opções de sabores vale o dinheiro gasto",
    "comprei para meu filho lanchar na escola quando ele tem aulas extras  ele amou",
    "muito gostosas"
]

# Função para análise de sentimento com VADER
def analisar_sentimento_vader(texto):
    polaridade = analyzer.polarity_scores(texto)["compound"]  # Varia de -1 a 1

    if polaridade > 0:
        return "Positivo ✅"
    elif polaridade < 0:
        return "Negativo ❌"
    else:
        return "Neutro ⚠️"

# Aplicar análise a todos os comentários
resultados_vader = {comentario: analisar_sentimento_vader(comentario) for comentario in comentarios_limpos}

# Exibir os resultados
for comentario, sentimento in resultados_vader.items():
    print(f"Comentário: {comentario} → Sentimento: {sentimento}")




































