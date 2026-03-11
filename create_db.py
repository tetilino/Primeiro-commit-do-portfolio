import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# USERS
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

cursor.execute("""
INSERT INTO users(username,password)
VALUES("admin","123")
""")

# PROJETOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS projetos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT
)
""")

cursor.execute("""
INSERT INTO projetos(nome)
VALUES
("Sistema CRM"),
("Site institucional"),
("App financeiro")
""")

# TAREFAS (KANBAN)
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
status TEXT
)
""")

cursor.execute("""
INSERT INTO tarefas(nome,status)
VALUES
("Criar site","todo"),
("Dashboard","doing"),
("Deploy","done")
""")

# CLIENTES
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
email TEXT,
empresa TEXT
)
""")

cursor.execute("""
INSERT INTO clientes(nome,email,empresa)
VALUES
("Maria Silva","maria@email.com","Loja Bella"),
("João Costa","joao@email.com","Tech Solutions")
""")

# FINANCEIRO
cursor.execute("""
CREATE TABLE IF NOT EXISTS financeiro(
id INTEGER PRIMARY KEY AUTOINCREMENT,
cliente TEXT,
valor REAL,
status TEXT
)
""")

cursor.execute("""
INSERT INTO financeiro(cliente,valor,status)
VALUES
("Maria Silva",2500,"Pago"),
("João Costa",1200,"Pendente")
""")

# ARQUIVOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS arquivos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
projeto TEXT
)
""")

cursor.execute("""
INSERT INTO arquivos(nome,projeto)
VALUES
("proposta.pdf","Sistema CRM"),
("layout.png","Site institucional")
""")

conn.commit()
conn.close()

print("BANCO CRIADO COM SUCESSO")