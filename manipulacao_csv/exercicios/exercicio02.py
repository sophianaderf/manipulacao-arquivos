import csv


def consultar_pokemons():

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = list(csv.DictReader(arquivo))

    while True:
        print("\n===== POKÉMON DOS TREINADORES =====")
        print("1 - Listar Pokémon de um treinador")
        print("2 - Contar Pokémon de um treinador")
        print("3 - Mostrar Pokémon de maior nível")
        print("4 - Mostrar Pokémon de menor nível")
        print("5 - Listar Pokémon de determinado tipo")
        print("6 - Voltar ao menu")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_treinador = input("Digite o nome do treinador: ")

            treinador_encontrado = False
            lista_pokemons = []

            for treinador in treinadores:
                if treinador["nome"] == nome_treinador:
                    treinador_encontrado = True

            if treinador_encontrado:
                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        lista_pokemons.append(pokemon)

                if len(lista_pokemons) > 0:
                    print("\n--- POKÉMON DO TREINADOR ---")

                    for pokemon in lista_pokemons:
                        print(f"Nome: {pokemon['nome']}")
                        print(f"Tipo: {pokemon['tipo']}")
                        print(f"Nível: {pokemon['nivel']}")
                        print()

                else:
                    print("Esse treinador não possui Pokémon cadastrados.")

            else:
                print("Treinador não encontrado.")

        elif opcao == "2":
            nome_treinador = input("Digite o nome do treinador: ")

            treinador_encontrado = False
            quantidade = 0

            for treinador in treinadores:
                if treinador["nome"] == nome_treinador:
                    treinador_encontrado = True

            if treinador_encontrado:
                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        quantidade += 1

                print(f"\nQuantidade de Pokémon: {quantidade}")

            else:
                print("Treinador não encontrado.")

        elif opcao == "3":
            nome_treinador = input("Digite o nome do treinador: ")

            treinador_encontrado = False
            lista_pokemons = []

            for treinador in treinadores:
                if treinador["nome"] == nome_treinador:
                    treinador_encontrado = True

            if treinador_encontrado:
                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        lista_pokemons.append(pokemon)

                if len(lista_pokemons) > 0:
                    maior_nivel = lista_pokemons[0]

                    for pokemon in lista_pokemons:
                        if int(pokemon["nivel"]) > int(maior_nivel["nivel"]):
                            maior_nivel = pokemon

                    print("\n--- POKÉMON DE MAIOR NÍVEL ---")
                    print(f"Nome: {maior_nivel['nome']}")
                    print(f"Tipo: {maior_nivel['tipo']}")
                    print(f"Nível: {maior_nivel['nivel']}")

                else:
                    print("Esse treinador não possui Pokémon cadastrados.")

            else:
                print("Treinador não encontrado.")

        elif opcao == "4":
            nome_treinador = input("Digite o nome do treinador: ")

            treinador_encontrado = False
            lista_pokemons = []

            for treinador in treinadores:
                if treinador["nome"] == nome_treinador:
                    treinador_encontrado = True

            if treinador_encontrado:
                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        lista_pokemons.append(pokemon)

                if len(lista_pokemons) > 0:
                    menor_nivel = lista_pokemons[0]

                    for pokemon in lista_pokemons:
                        if int(pokemon["nivel"]) < int(menor_nivel["nivel"]):
                            menor_nivel = pokemon

                    print("\n--- POKÉMON DE MENOR NÍVEL ---")
                    print(f"Nome: {menor_nivel['nome']}")
                    print(f"Tipo: {menor_nivel['tipo']}")
                    print(f"Nível: {menor_nivel['nivel']}")

                else:
                    print("Esse treinador não possui Pokémon cadastrados.")

            else:
                print("Treinador não encontrado.")

        elif opcao == "5":
            tipo = input("Digite o tipo do Pokémon: ")

            encontrado = False

            print("\n--- POKÉMON DO TIPO ---")

            for pokemon in pokemons:
                if pokemon["tipo"] == tipo:
                    print(f"Nome: {pokemon['nome']}")
                    print(f"Tipo: {pokemon['tipo']}")
                    print(f"Nível: {pokemon['nivel']}")
                    print(f"Treinador: {pokemon['treinador']}")
                    print()

                    encontrado = True

            if encontrado == False:
                print("Nenhum Pokémon desse tipo foi encontrado.")

        elif opcao == "6":
            print("Voltando ao menu...")
            break

        else:
            print("Opção inválida!")


consultar_pokemons()