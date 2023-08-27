import sqlite3

conexao = sqlite3.connect("prova.db")

conexao.execute('''CREATE TABLE IF NOT EXISTS aluno
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOT NULL);
                ''')

def cria_aluno(conexao, nome, idade):
    conexao.execute("INSERT INTO aluno(nome, idade) VALUES (?,?);", (nome,idade))
    conexao.commit()
    print("Aluno inserido com sucesso!")
    return novo_aluno

def listar_alunos(conexao):
    alunos = conexao.execute("SELECT * FROM aluno;")
    for aluno in alunos:
        print(aluno)

    return alunos

def atualizar_aluno(conexao, id, novo_nome, nova_idade):
    conexao.execute("UPDATE aluno SET nome = ?, idade = ? WHERE id = ?;", (novo_nome, nova_idade, id))
    conexao.commit()
    print("Aluno atualizado corretamente")
    return aluno_atualizado 

def deletar_aluno(conexao, id):
    conexao.execute("DELETE FROM aluno WHERE id = ?;", (id,))
    print("Aluno deletado corretamente")

atualizar_aluno(3, "Teste", "15")

deletar_aluno(3)
listar_alunos()