 #turma=[]
def criarturma():
    print("Turma criada com sucesso.")
    turma = []
    return turma

def inseriralunonaturma(turma):
    nome = input("Introduza o nome do aluno:")
    id = int(input("Introduza o id do aluno:"))
    for a in turma:
        while id == a[1]:
            print("Já existe um aluno com esse id.")
            id = int(input("Introduza o id do aluno:"))
    hw = float(input("Introduza a nota do TPC:"))
    while hw < 0 or hw > 20:
        print("Nota inválida. (Nota deve estar entre 0 e 20 valores)")
        hw = float(input("Introduza a nota do TPC:"))
    projectgrade = float(input("Introduza a nota do projeto:"))
    while projectgrade < 0 or projectgrade > 20:
        print("Nota inválida. (Nota deve estar entre 0 e 20 valores)")
        projectgrade = float(input("Introduza a nota do projeto:"))
    test = float(input("Introduza a nota do teste:"))
    while test < 0 or test > 20:
        print("Nota inválida. (Nota deve estar entre 0 e 20 valores)")
        test = float(input("Introduza a nota do teste:"))
    aluno = (nome, id, [hw, projectgrade, test])
    turma.append(aluno)

def listarTurma(turma):
    print("Listagem dos alunos da turma:")
    for a in turma:
        print(a)

def consultarAluno(turma):
    id = int(input("Introduza o id do aluno que deseja consultar:"))
    found = False
    for a in turma:
        if a[1] == id:
            print(a)
            found = True
    if not found:
        print(f"O aluno com o id {id} não se encontra na turma.")

def linha(aluno):
    nome, id, notas = aluno
    return f"{nome},{id},{notas[0]},{notas[1]},{notas[2]}\n"

def guardarTurma(turma, name):
    file = open(name, "w")
    for aluno in turma:
        file.write(linha(aluno))
    file.close()

def carregar_turma():
    nome_arquivo = input("Nome do arquivo para carregar a turma (ex: turma.txt): ")
    global turma
    turma = []
    file = open(nome_arquivo, "r")
    linhas = file.readlines()
    for linha in linhas:
        dados = linha.strip().split(',')
        if len(dados) == 5:
            nome = dados[0]
            id = int(dados[1])
            hw = float(dados[2])
            projectgrade = float(dados[3])
            test = float(dados[4])
            aluno = (nome, id, [hw, projectgrade, test])
            turma.append(aluno)
    file.close()
    print(f"Turma carregada do arquivo {nome_arquivo}.")

def menu():
    print("""
    1. Criar Turma
    2. Inserir aluno
    3. Listar turma
    4. Consultar aluno por id
    5. Guardar turma
    6. Carregar uma turma de um ficheiro
    0. Sair da aplicação
    """)
    choice = int(input("Qual opção deseja selecionar? "))
    return choice

option = menu()
while option != 0:
    if option == 1:
        turma = criarturma()
    elif option == 2:
        inseriralunonaturma(turma)
        print("Aluno inserido com sucesso.")
    elif option == 3:
        if len(turma) == 0:
            print("Ainda não existem turmas.")
        else:
            listarTurma(turma)
    elif option == 4:
        if len(turma) == 0:
            print("Ainda não existem turmas.")
        else:
            consultarAluno(turma)
    elif option == 5:
        if len(turma) == 0:
            print("Ainda não existem turmas.")
        else:
            guardarTurma(turma, "turma.txt")
            print("Turma guardada com sucesso.")
    elif option == 6:
        carregar_turma()
    else:
        print("Opção inválida, tente novamente.")
    option = menu()

print("Obrigado e até à próxima!")
