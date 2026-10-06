import csv


def campeonato_pokemon():

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = list(csv.DictReader(arquivo))

    resultados = []

    while True:
        print("\n===== CAMPEONATO POKÉMON =====")
        print("1 - Listar treinadores")
        print("2 - Consultar equipe")
        print("3 - Calcular pontuação")
        print("4 - Mostrar classificação")
        print("5 - Gerar arquivo CSV do campeonato")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            print("\n===== TREINADORES =====")

            for treinador in treinadores:
                print(f"Nome: {treinador['nome']}")
                print(f"Região: {treinador['regiao']}")
                print(f"Nível: {treinador['nivel']}")
                print()


        elif opcao == "2":
            nome = input("Digite o nome do treinador: ")

            encontrado = False

            for treinador in treinadores:
                if treinador["nome"] == nome:
                    print(f"\nTreinador: {treinador['nome']}")
                    print(f"Região: {treinador['regiao']}")
                    print(f"Nível: {treinador['nivel']}")

                    print("\nPokémon da equipe:")

                    contador = 1

                    for pokemon in pokemons:
                        if pokemon["treinador"] == nome:
                            print(f"{contador} - {pokemon['nome']} - {pokemon['tipo']} - {pokemon['nivel']}")
                            contador += 1

                    encontrado = True

            if encontrado == False:
                print("Treinador não encontrado.")


        elif opcao == "3":
            resultados = []

            for treinador in treinadores:

                nome = treinador["nome"]
                nivel_treinador = int(treinador["nivel"])

                quantidade_pokemons = 0
                soma_niveis = 0

                for pokemon in pokemons:
                    if pokemon["treinador"] == nome:
                        quantidade_pokemons += 1
                        soma_niveis += int(pokemon["nivel"])

                pontuacao = nivel_treinador + soma_niveis

                resultado = {
                    "treinador": nome,
                    "regiao": treinador["regiao"],
                    "nivel_treinador": nivel_treinador,
                    "quantidade_pokemons": quantidade_pokemons,
                    "soma_niveis": soma_niveis,
                    "pontuacao": pontuacao
                }

                resultados.append(resultado)

            print("\n===== PONTUAÇÃO =====")

            for resultado in resultados:
                print(f"Treinador: {resultado['treinador']}")
                print(f"Região: {resultado['regiao']}")
                print(f"Nível do treinador: {resultado['nivel_treinador']}")
                print(f"Quantidade de Pokémon: {resultado['quantidade_pokemons']}")
                print(f"Soma dos níveis: {resultado['soma_niveis']}")
                print(f"Pontuação: {resultado['pontuacao']}")
                print()


        elif opcao == "4":

            if len(resultados) == 0:
                print("Calcule a pontuação primeiro.")
            else:
                classificacao = sorted(
                    resultados,
                    key=lambda resultado: resultado["pontuacao"],
                    reverse=True
                )

                print("\n===== CLASSIFICAÇÃO =====")

                posicao = 1

                for resultado in classificacao:
                    print(
                        f"{posicao}º - {resultado['treinador']} - "
                        f"{resultado['pontuacao']} pontos"
                    )
                    posicao += 1


        elif opcao == "5":

            if len(resultados) == 0:
                print("Calcule a pontuação primeiro.")
            else:
                with open(
                    "resultado_campeonato.csv",
                    "w",
                    newline="",
                    encoding="utf-8"
                ) as arquivo:

                    campos = [
                        "treinador",
                        "regiao",
                        "nivel_treinador",
                        "quantidade_pokemons",
                        "soma_niveis",
                        "pontuacao"
                    ]

                    escritor = csv.DictWriter(
                        arquivo,
                        fieldnames=campos
                    )

                    escritor.writeheader()

                    for resultado in resultados:
                        escritor.writerow(resultado)

                print("Arquivo resultado_campeonato.csv criado com sucesso!")


        elif opcao == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


campeonato_pokemon()