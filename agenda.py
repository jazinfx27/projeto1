import sqlite3

# Conectar ou criar o banco de dados
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT,
        cpf TEXT,
        endereco TEXT
    )
''')
conexao.commit()

# Função para adicionar contato
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    cursor.execute('''
        INSERT INTO contatos (nome, telefone, email, cpf, endereco)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, telefone, email, cpf, endereco))
    conexao.commit()
    print("Contato adicionado com sucesso!")

# Função para listar todos os contatos
def listar_contatos():
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    for contato in contatos:
        print(f'''
ID: {contato[0]}
Nome: {contato[1]}
Telefone: {contato[2]}
Email: {contato[3]}
CPF: {contato[4]}
Endereço: {contato[5]}
-----------------------
''')

# Função para buscar contato por nome
def buscar_contato():
    nome = input("Digite o nome para buscar: ")
    cursor.execute("SELECT * FROM contatos WHERE nome LIKE ?", ('%' + nome + '%',))
    contatos = cursor.fetchall()
    for contato in contatos:
        print(f'''
ID: {contato[0]}
Nome: {contato[1]}
Telefone: {contato[2]}
Email: {contato[3]}
CPF: {contato[4]}
Endereço: {contato[5]}
-----------------------
''')

# Função para remover contato por ID
def remover_contato():
    id_contato = input("Digite o ID do contato a ser removido: ")
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id_contato,))
    conexao.commit()
    print("Contato removido com sucesso!")

# Menu principal
def menu():
    while True:
        print("""
=== AGENDA DE CONTATOS ===
1 - Adicionar contato
2 - Listar contatos
3 - Buscar contato
4 - Remover contato
5 - Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            remover_contato()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Executar menu
menu()

# Fechar conexão com o banco
cursor.close()
conexao.close()
