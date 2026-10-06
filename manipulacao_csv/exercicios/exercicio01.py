import csv


def consultar_treinadores():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = csv.DictReader(arquivo)

        lista_treinadores = list(treinadores)

        while True:
            print("\n===== TREINADORES POKÉMON =====")
            print("1 - Listar todos os treinadores")
            print("2 - Buscar treinador pelo nome")
            print("3 - Listar treinadores de uma região")
            print("4 - Mostrar treinador com maior nível")
            print("5 - Mostrar treinador com menor nível")
            print("6 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\n--- TODOS OS TREINADORES ---")

                for treinador in lista_treinadores:
                    print(f"Nome: {treinador['nome']}")
                    print(f"Região: {treinador['regiao']}")
                    print(f"Nível: {treinador['nivel']}")
                    print()

            elif opcao == "2":
                nome = input("Digite o nome do treinador: ")

                encontrado = False

                for treinador in lista_treinadores:
                    if treinador["nome"] == nome:
                        print("\nTreinador encontrado!")
                        print(f"Nome: {treinador['nome']}")
                        print(f"Região: {treinador['regiao']}")
                        print(f"Nível: {treinador['nivel']}")
                        encontrado = True

                if encontrado == False:
                    print("Treinador não encontrado.")

            elif opcao == "3":
                regiao = input("Digite a região: ")

                encontrado = False

                for treinador in lista_treinadores:
                    if treinador["regiao"] == regiao:
                        print(f"\nNome: {treinador['nome']}")
                        print(f"Região: {treinador['regiao']}")
                        print(f"Nível: {treinador['nivel']}")
                        encontrado = True

                if encontrado == False:
                    print("Nenhum treinador encontrado nessa região.")

            elif opcao == "4":
                maior_nivel = lista_treinadores[0]

                for treinador in lista_treinadores:
                    if int(treinador["nivel"]) > int(maior_nivel["nivel"]):
                        maior_nivel = treinador

                print("\n--- TREINADOR COM MAIOR NÍVEL ---")
                print(f"Nome: {maior_nivel['nome']}")
                print(f"Região: {maior_nivel['regiao']}")
                print(f"Nível: {maior_nivel['nivel']}")

            elif opcao == "5":
                menor_nivel = lista_treinadores[0]

                for treinador in lista_treinadores:
                    if int(treinador["nivel"]) < int(menor_nivel["nivel"]):
                        menor_nivel = treinador

                print("\n--- TREINADOR COM MENOR NÍVEL ---")
                print(f"Nome: {menor_nivel['nome']}")
                print(f"Região: {menor_nivel['regiao']}")
                print(f"Nível: {menor_nivel['nivel']}")

            elif opcao == "6":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida!")


consultar_treinadores()