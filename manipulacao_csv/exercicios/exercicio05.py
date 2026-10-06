import csv


def gerenciar_pokemons():

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = list(csv.DictReader(arquivo))

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    while True:
        print("\n===== GERENCIADOR DE POKÉMON =====")
        print("1 - Listar Pokémon")
        print("2 - Pesquisar Pokémon")
        print("3 - Adicionar Pokémon")
        print("4 - Alterar nível de um Pokémon")
        print("5 - Remover Pokémon")
        print("6 - Salvar alterações")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

     
        if opcao == "1":

            print("\n===== POKÉMON CADASTRADOS =====")

            for pokemon in pokemons:
                print(f"Nome: {pokemon['nome']}")
                print(f"Tipo: {pokemon['tipo']}")
                print(f"Nível: {pokemon['nivel']}")
                print(f"Treinador: {pokemon['treinador']}")
                print()


        elif opcao == "2":

            nome = input("Digite o nome do Pokémon: ")

            encontrado = False

            for pokemon in pokemons:
                if pokemon["nome"] == nome:
                    print("\nPokémon encontrado!")
                    print(f"Nome: {pokemon['nome']}")
                    print(f"Tipo: {pokemon['tipo']}")
                    print(f"Nível: {pokemon['nivel']}")
                    print(f"Treinador: {pokemon['treinador']}")

                    encontrado = True

            if encontrado == False:
                print("Pokémon não encontrado.")


        elif opcao == "3":

            nome = input("Digite o nome do Pokémon: ")

            if nome == "":
                print("O nome não pode ficar vazio.")

            else:
                encontrado = False

                for pokemon in pokemons:
                    if pokemon["nome"] == nome:
                        encontrado = True

                if encontrado:
                    print("Esse Pokémon já existe.")

                else:
                    tipo = input("Digite o tipo: ")

                    if tipo == "":
                        print("O tipo não pode ficar vazio.")

                    else:
                        nivel = int(input("Digite o nível: "))

                        if nivel < 1 or nivel > 100:
                            print("O nível deve estar entre 1 e 100.")

                        else:
                            treinador = input("Digite o treinador: ")

                            treinador_existe = False

                            for pessoa in treinadores:
                                if pessoa["nome"] == treinador:
                                    treinador_existe = True

                            if treinador_existe:

                                novo_pokemon = {
                                    "nome": nome,
                                    "tipo": tipo,
                                    "nivel": str(nivel),
                                    "treinador": treinador
                                }

                                pokemons.append(novo_pokemon)

                                print("Pokémon adicionado com sucesso!")

                            else:
                                print("Treinador não encontrado.")


        elif opcao == "4":

            nome = input("Digite o nome do Pokémon: ")

            encontrado = False

            for pokemon in pokemons:
                if pokemon["nome"] == nome:

                    novo_nivel = int(input("Digite o novo nível: "))

                    if novo_nivel >= 1 and novo_nivel <= 100:
                        pokemon["nivel"] = str(novo_nivel)

                        print("Nível alterado com sucesso!")

                    else:
                        print("O nível deve estar entre 1 e 100.")

                    encontrado = True

            if encontrado == False:
                print("Pokémon não encontrado.")


        elif opcao == "5":

            nome = input("Digite o nome do Pokémon que deseja remover: ")

            encontrado = False

            for pokemon in pokemons:
                if pokemon["nome"] == nome:
                    pokemons.remove(pokemon)
                    encontrado = True
                    print("Pokémon removido com sucesso!")
                    break

            if encontrado == False:
                print("Pokémon não encontrado.")

        # OPÇÃO 6 - SALVAR
        elif opcao == "6":

            with open("pokemons_atualizados.csv", "w", newline="", encoding="utf-8") as arquivo:

                campos = ["nome", "tipo", "nivel", "treinador"]

                escritor = csv.DictWriter(
                    arquivo,
                    fieldnames=campos
                )

                escritor.writeheader()

                for pokemon in pokemons:
                    escritor.writerow(pokemon)

            print("Alterações salvas com sucesso!")
            print(f"Quantidade de Pokémon salvos: {len(pokemons)}")


        elif opcao == "7":

            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


gerenciar_pokemons()