cadastro_alunos.py

def menu():
    print("\n=== Cadastro de Alunos ===")
    print("1 - Cadastrar Novo Aluno")
    print("2 - Listar Alunos Cadastrados")
    print("3 - Buscar Aluno por Matrícula")
    print("4 - Sair")
def cadastrar_aluno(lista_alunos):
    print("\n--- Cadastro de Novo Aluno ---")
    nome = input("Nome do aluno: ").strip()
    curso = input("Curso: ").strip()
    while True:
        try:
            matricula = int(input("Número de matrícula (somente números): "))
            break
        except ValueError:
            print(" Matrícula inválida! Digite apenas números.")

    aluno = {"nome": nome, "matricula": matricula, "curso": curso}
    lista_alunos.append(aluno)
    print(" Aluno cadastrado com sucesso!")
def listar_alunos(lista_alunos):
    print("\n--- Alunos Cadastrados ---")
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for idx, aluno in enumerate(lista_alunos, start=1):
            print(f"{idx}. Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}")
def buscar_por_matricula(lista_alunos):
    print("\n--- Buscar Aluno por Matrícula ---")
    try:
        matricula = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print(" Valor inválido! Digite apenas números.")
        return

    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            print(f" Aluno encontrado: Nome: {aluno['nome']} | Curso: {aluno['curso']}")
            return
    print(" Aluno não encontrado.")


def main():
    alunos = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_por_matricula(alunos)
        elif opcao == "4":
            print("Saindo do programa... ")
            break
        else:
            print(" Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
