import os 
os.system("clear")


produtos = []
def cadastrar_produto():
    
    print("\n--- Cadastrar Produto ---")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade em estoque: "))
    produtos.append([nome, preco, quantidade])
    print(f"'{nome}' cadastrado!")

def mostrar_produtos():
    
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return


    for i, produto in enumerate(produtos):
       
        print(f"{i+1}. {produto[0]} - R${produto[1]:.2f} - Estoque: {produto[2]}")

def registrar_venda():
   
    print("\n--- Registrar Venda ---")
    if not produtos:
        print("Nenhum produto para vender.")
        return

    nome_venda = input("Nome do produto a vender: ")
    qtd_venda = int(input("Quantidade a vender: "))

    encontrado = False
    for produto in produtos:
        if produto[0].lower() == nome_venda.lower(): 
            encontrado = True
            if produto[2] >= qtd_venda:
                produto[2] -= qtd_venda
                valor_total = produto[1] * qtd_venda
                print(f"Venda de {qtd_venda} de '{produto[0]}' realizada. Total: R${valor_total:.2f}")
            else:
                print(f"Estoque insuficiente para '{produto[0]}'. Disponível: {produto[2]}")
            break 
    if not encontrado:
        print(f"Produto '{nome_venda}' não encontrado.")

def atualizar_estoque():

    print("\n--- Atualizar Estoque ---")
    if not produtos:
        print("Nenhum produto para atualizar.")
        return

    nome_atualizar = input("Nome do produto para atualizar: ")
    nova_qtd = int(input("Nova quantidade em estoque: "))

    encontrado = False
    for produto in produtos:
        if produto[0].lower() == nome_atualizar.lower():
            encontrado = True
            produto[2] = nova_qtd 
            print(f"Estoque de '{produto[0]}' atualizado para {nova_qtd}.")
            break
    if not encontrado:
        print(f"Produto '{nome_atualizar}' não encontrado.")

def main():
    
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Registrar Venda")
        print("4. Atualizar Estoque")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            mostrar_produtos()
        elif opcao == '3':
            registrar_venda()
        elif opcao == '4':
            atualizar_estoque()
        elif opcao == '5':
            print("Saindo do sistema!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()