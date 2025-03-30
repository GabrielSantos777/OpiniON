import sys
sys.stdout.reconfigure(encoding='utf-8')

import scripts.coletar_comentarios as coletar_comentarios
import scripts.processar_comentarios as processar_comentarios
import scripts.analise_sentimento as analise_sentimento
import scripts.resumo as resumo
import scripts.visualizar_sentimentos as visualizar_sentimentos

if __name__ == "__main__":
    print("🔵 Iniciando o processo completo...")

    # Passo 1: Coletar os comentários da Amazon
    print("🟡 Coletando comentários...")
    coletar_comentarios.coletar_e_salvar()

    # Passo 2: Processar os comentários
    print("🟡 Processando os comentários...")
    processar_comentarios.processar_comentarios()

    # Passo 3: Analisar sentimentos
    print("🟡 Analisando os sentimentos...")
    analise_sentimento.analisar_sentimentos()

    # Passo 4: Gerar o gráfico de sentimentos
    print("🟡 Gerando gráfico...")
    visualizar_sentimentos.exibir_grafico()

    # Passo 5: Gerar o resumo do produto
    print("🟡 Gerando o resumo...")
    resumo.exibir_resumo()

    print("✅ Processo finalizado com sucesso!")
