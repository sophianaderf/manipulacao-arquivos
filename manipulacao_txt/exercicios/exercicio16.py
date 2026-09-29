def buscar_produto():
    produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            produto = {
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            }

            produtos.append(produto)

    nome_pesquisa = input("Digite o produto: ")

    for produto in produtos:
        if produto["nome"] == nome_pesquisa:
            print("Produto encontrado!")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            return

    print("Produto não encontrado!")


buscar_produto()