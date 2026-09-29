def criar_arquivo():
    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Bruno\n")
        arquivo.write("Carlos\n")
        arquivo.write("Daniela\n")
        arquivo.write("Eduardo\n")
        arquivo.write("Fernanda\n")


def contar_linhas():
    contador = 0

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            contador += 1

    print(f"O arquivo possui {contador} linhas.")


criar_arquivo()
contar_linhas()