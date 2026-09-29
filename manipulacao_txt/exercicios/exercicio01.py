def ler_arquivo():
    with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    print(conteudo)


ler_arquivo()