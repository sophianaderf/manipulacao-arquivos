import csv


def relatorios():

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = list(csv.DictReader(arquivo))

    while True:
        print("\n===== RELATÓRIOS =====")
        print("1 - Relatório de um treinador")
        print("2 - Média de nível dos Pokémon de um treinador")
        print("3 - Média de nível dos Pokémon por tipo")
        print("4 - Quantidade de Pokémon por treinador")
        print("5 - Quantidade de Pokémon por tipo")
        print("6 - Treinadores com nível acima de um valor")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        # OPÇÃO 1
        if opcao == "1":
            nome_treinador = input("Digite o nome do treinador: ")

            treinador_encontrado = False
            lista_pokemons = []

            for treinador in treinadores:
                if treinador["nome"] == nome_treinador:
                    treinador_encontrado = True

                    print("\n===== RELATÓRIO DO TREINADOR =====")
                    print(f"Treinador: {treinador['nome']}")
                    print(f"Região: {treinador['regiao']}")
                    print(f"Nível do treinador: {treinador['nivel']}")

            if treinador_encontrado:
                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        lista_pokemons.append(pokemon)

                print("\nPokémon:")

                for pokemon in lista_pokemons:
                    print(f"- {pokemon['nome']} - {pokemon['tipo']} - Nível {pokemon['nivel']}")

            else:
                print("Treinador não encontrado.")


        elif opcao == "2":
            nome_treinador = input("Digite o nome do treinador: ")

            treinador_encontrado = False
            soma = 0
            quantidade = 0

            for treinador in treinadores:
                if treinador["nome"] == nome_treinador:
                    treinador_encontrado = True

            if treinador_encontrado:

                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        nivel = int(pokemon["nivel"])
                        soma += nivel
                        quantidade += 1

                if quantidade > 0:
                    media = soma / quantidade

                    print(f"\nMédia de nível dos Pokémon de {nome_treinador}: {media:.2f}")

                else:
                    print("Esse treinador não possui Pokémon.")

            else:
                print("Treinador não encontrado.")


        elif opcao == "3":
            tipo = input("Digite o tipo dos Pokémon: ")

            soma = 0
            quantidade = 0

            for pokemon in pokemons:
                if pokemon["tipo"] == tipo:
                    nivel = int(pokemon["nivel"])
                    soma += nivel
                    quantidade += 1

            if quantidade > 0:
                media = soma / quantidade

                print(f"\nMédia de nível dos Pokémon do tipo {tipo}: {media:.2f}")

            else:
                print("Nenhum Pokémon desse tipo foi encontrado.")


        elif opcao == "4":
            quantidade_treinadores = {}

            for pokemon in pokemons:
                treinador = pokemon["treinador"]

                if treinador in quantidade_treinadores:
                    quantidade_treinadores[treinador] += 1

                else:
                    quantidade_treinadores[treinador] = 1

            print("\n===== QUANTIDADE DE POKÉMON POR TREINADOR =====")

            resultados = sorted(
                quantidade_treinadores.items(),
                key=lambda item: item[1],
                reverse=True
            )

            for treinador, quantidade in resultados:
                print(f"{treinador}: {quantidade}")


        elif opcao == "5":
            quantidade_tipos = {}

            for pokemon in pokemons:
                tipo = pokemon["tipo"]

                if tipo in quantidade_tipos:
                    quantidade_tipos[tipo] += 1

                else:
                    quantidade_tipos[tipo] = 1

            print("\n===== QUANTIDADE DE POKÉMON POR TIPO =====")

            resultados = sorted(
                quantidade_tipos.items(),
                key=lambda item: item[1],
                reverse=True
            )

            for tipo, quantidade in resultados:
                print(f"{tipo}: {quantidade}")


        elif opcao == "6":
            nivel_minimo = int(input("Digite o nível mínimo: "))

            encontrado = False

            print("\n===== TREINADORES ACIMA DO NÍVEL =====")

            for treinador in treinadores:
                nivel = int(treinador["nivel"])

                if nivel > nivel_minimo:
                    print(f"{treinador['nome']} - Nível {treinador['nivel']}")
                    encontrado = True

            if encontrado == False:
                print("Nenhum treinador possui nível acima desse valor.")


        elif opcao == "7":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


relatorios()