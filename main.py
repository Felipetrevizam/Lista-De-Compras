# Lista de Compras

lista = []

while True:
    questao = input("Você que inserir um produto (I) \nVocê quer escluir um produto (E)\nVocê quer ordenar a lista? (O)\nSair do programa (S)\nEscolha: ")
    if questao == 'I' or questao == 'i':
        produto = input("Insira o produto: ")
        lista.append(produto)
        print('\n')
    elif questao == 'E' or questao == 'e':
        produto = input("Qual produto você quer excluir? ")
        if produto in lista:
            lista.remove(produto)
        else:
            print("Produto não encontrado na lista.")
    elif questao == 'O' or questao == 'o':
        print("\n")
        for i, produto in enumerate(lista):
            print(f"Índice: {i}, Produto: {produto}")
        print('\n')
    elif questao == 'S' or questao == 's':
        break
    else:
        print("Comando inválido\n")
