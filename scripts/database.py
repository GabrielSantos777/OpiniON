import sqlite3

def criar_tabela():
    conn = sqlite3.connect("data/raw/comentarios_analise.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            comentario TEXT NOT NULL,
            data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados configurado com sucesso!")


if __name__ == "__main__":
    criar_tabela()
