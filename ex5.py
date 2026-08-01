def mostrar_menu():
    print("\n" + "=" * 40)
    print("         sistema de controle de Produtos")
    print("=" * 45)
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Consultar Produto")
    print("4 - Calcular valor total do estoque")
    print("5 - Excluir Produto")
    print("0 - Sair")
    print("=" * 45)

def cadastrar_produto():
    print("\n" + "=" * 40)
    print("         Cadastro de Produto")
    print("=" * 45)
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    return (nome, preco, quantidade)

def listar_produtos(produtos):
    print("\n" + "=" * 40)
    print("         Lista de Produtos")
    print("=" * 45)
    for produto in produtos:
        print(f"Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}")

def consultar_produto(produtos, nome):
    for produto in produtos:
        if produto[0] == nome:
            return produto
    return None

def calcular_valor_total_estoque(produtos):
    total = 0
    for produto in produtos:
        total += produto[1] * produto[2]
    return total

def excluir_produto(produtos, nome):
    for i, produto in enumerate(produtos):
        if produto[0] == nome:
            del produtos[i]
            return True
    return False

def main():
    produtos = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            produto = cadastrar_produto()
            produtos.append(produto)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            nome = input("Digite o nome do produto a consultar: ")
            produto = consultar_produto(produtos, nome)
            if produto:
                print(f"Produto encontrado: Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}")
            else:
                print("Produto não encontrado.")
        elif opcao == "4":
            total = calcular_valor_total_estoque(produtos)
            print(f"Valor total do estoque: {total}")
        elif opcao == "5":
            nome = input("Digite o nome do produto a excluir: ")
            if excluir_produto(produtos, nome):
                print("Produto excluído com sucesso.")
            else:
                print("Produto não encontrado.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
main()