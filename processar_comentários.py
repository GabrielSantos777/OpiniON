import re

# Lista de comentários coletados
comentarios = [
    "Muito gostoso.\nVale o investimento. Muito bom. Minha nutricionista recomenda.",
    "Muito bom e com a possibilidade de experimentar diferentes sabores",
    "Melhor barrinha. Pena que é tão cara, só dá p comprar na promo",
    "Essa barrinha é uma delícia e realmente satisfaz pela quantidade de proteína, compro direto e amo.",
    "Realmente tem sabores muito bons para uma barra de proteina, mas tem outros que nem tanto. A barrinha é boa mas é mt cara, vale a experiência",
    "Produto bom, chegou no prazo estimado, veio bem embalado e são muitas opções de sabores. Vale o dinheiro gasto.",
    "Comprei para meu filho lanchar na escola quando ele tem aulas extras . Ele amou .",
    "muito gostosas"
]

def limpar_texto(texto):
    texto = texto.lower()  # Converte para minúsculas
    texto = re.sub(r'\n', ' ', texto)  # Remove quebras de linha
    texto = re.sub(r'[^a-zA-Zá-úÁ-Ú0-9 ]', '', texto)  # Remove caracteres especiais
    return texto.strip()

comentarios_limpos = [limpar_texto(c) for c in comentarios]

print("Comentários limpos:")
print(comentarios_limpos)
