def sistema_alunos():
    with open("alunos.txt", "w") as arquivo:
        arquivo.write("1;Ana Silva;17;Desenvolvimento de Sistemas\n")
        arquivo.write("2;Bruno Souza;18;Desenvolvimento de Sistemas")

    alunos = []

    with open("alunos.txt") as arquivo:
        for linha in arquivo:
            id, nome, idade, curso = linha.strip().split(";")
            alunos.append({
                "id": int(id),
                "nome": nome,
                "idade": int(idade),
                "curso": curso
            })

    while True:
        print("1-Listar 2-Buscar 3-Cadastrar 4-Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            print(alunos)

        elif opcao == "2":
            id = int(input("ID: "))

            for aluno in alunos:
                if aluno["id"] == id:
                    print(aluno)

        elif opcao == "3":
            id = int(input("ID: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            alunos.append({
                "id": id,
                "nome": nome,
                "idade": idade,
                "curso": curso
            })

        elif opcao == "4":
            break


sistema_alunos()