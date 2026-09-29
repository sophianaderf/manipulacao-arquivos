def criar_arquivo():
    with open("texto.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Python é uma linguagem de programação.\n")
        arquivo.write("Python pode ser utilizada para desenvolvimento web.\n")
        arquivo.write("Python também é muito utilizada em ciência de dados.")


def contar_palavras():
    with open("texto.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()

    print(f"Quantidade de palavras: {len(palavras)}")


criar_arquivo()
contar_palavras()