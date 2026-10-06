import csv


def gerador_csv():

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = list(csv.DictReader(arquivo))

    while True:
        print("\n===== GERADOR DE ARQUIVOS =====")
        print("1 - Listar treinadores")
        print("2 - Gerar CSV de um treinador")
        print("3 - Gerar CSV de todos os treinadores")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n===== TREINADORES =====")

            for treinador in treinadores:
                print(treinador["nome"])

        elif opcao == "2":
            nome_treinador = input("Digite o treinador: ")

            treinador_encontrado = False
            lista_pokemons = []

            for treinador in treinadores:
                if treinador["nome"] == nome_treinador:
                    treinador_encontrado = True

            if treinador_encontrado:

                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        lista_pokemons.append(pokemon)

                nome_arquivo = nome_treinador.replace(" ", "_")
                nome_arquivo = "pokemons_" + nome_arquivo + ".csv"

                with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:

                    campos = ["nome", "tipo", "nivel", "treinador"]

                    escritor = csv.DictWriter(
                        arquivo,
                        fieldnames=campos
                    )

                    escritor.writeheader()

                    for pokemon in lista_pokemons:
                        escritor.writerow(pokemon)

                print(f"\nArquivo {nome_arquivo} criado com sucesso!")
                print(f"Quantidade de registros gravados: {len(lista_pokemons)}")

            else:
                print("Treinador não encontrado.")

        elif opcao == "3":

            pokemons_ordenados = sorted(
                pokemons,
                key=lambda pokemon: int(pokemon["nivel"])
            )

            nome_arquivo = "todos_pokemons_ordenados.csv"

            with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:

                campos = ["nome", "tipo", "nivel", "treinador"]

                escritor = csv.DictWriter(
                    arquivo,
                    fieldnames=campos
                )

                escritor.writeheader()

                for pokemon in pokemons_ordenados:
                    escritor.writerow(pokemon)

            print(f"\nArquivo {nome_arquivo} criado com sucesso!")
            print(f"Quantidade de registros gravados: {len(pokemons_ordenados)}")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


gerador_csv()