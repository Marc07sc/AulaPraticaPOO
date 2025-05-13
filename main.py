from app.logica_sistema import listar_alunos, cadastrar_aluno, deletar_aluno, detalhar_aluno

comando = ""
while comando != "5":
    comando = input(f"Escolha uma opção: \n"
                    f"1. Cadastrar Aluno \n"
                    f"2. Listar Alunos \n"
                    f"3. Detalhar Aluno\n"
                    f"4. Deletar Aluno\n"
                    f"5. Sair do sistema \n")

    match comando:
        case "1":
            nome = input("Informe o nome do aluno: ")
            nascimento = input("Informe a data de nascimento do aluno: ")
            curso = input("Informe o curso do aluno se tiver, se não deixe vazio: ")

            print(cadastrar_aluno(nome, nascimento, curso))

        case "2":
            print(listar_alunos())

        case "3":
            matricula = input("Informe a matrícula do aluno: ")

            print(detalhar_aluno(matricula))

        case "4":
            matricula = input("Informe a matrícula do aluno: ")

            print(deletar_aluno(matricula))

        case "5":
            print("Saindo do sistema.")