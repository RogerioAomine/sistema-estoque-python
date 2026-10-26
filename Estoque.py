estoque = [
    {"Nome":"Arroz","Preço": 10.00, "Quantidade": 20},
    {"Nome":"Feijão","Preço":20.00, "Quantidade": 2}
    ]


def valor_total(estoque):
    for armazenado in estoque:
        if armazenado['Quantidade'] < 10:
            restantes = 10 - armazenado["Quantidade"]
            valor_necessario = restantes * armazenado["Preço"]
            print(f"""
    ====================================
    
    PRODUTO = {armazenado['Nome']}
    QUANTIDADE A COMPRA: {restantes}
    VALOR A GASTA:{valor_necessario}

    ====================================

""" )

def baixo_estoque(estoque):
    for armazenado in estoque:
        if armazenado['Quantidade'] < 10:
            print(f"""Nome: {armazenado['Nome']}
A baixo da media de estoque em quantidade: {armazenado['Quantidade']}
Preço: {armazenado['Preço']}""")
            

def adicionar_estoque(estoque):
    nome_add = input("Digite o novo item:")
    preco_add = int(input("Valor que vc pagou:"))
    quantidade_add = int(input("Quantidade que vc comprou:"))

    estoque.append({
        "Nome": nome_add,
        "Preço": preco_add,
        "Quantidade": quantidade_add
        })

    for armazenado in estoque:
        print(f"""Armazenado em seu estoque temos: {armazenado['Nome']}
Preço dos produtos são: {armazenado ['Preço']}
Quantidade: {armazenado['Quantidade']}""")
        print("======================================")



def verificar_estoque(estoque):
    for armazenado in estoque:
        print(f"""Armazenado em seu estoque temos: {armazenado['Nome']}
Preço dos produtos são: {armazenado ['Preço']}
Quantidade: {armazenado['Quantidade']}""")
        print("======================================")



def menu(estoque):
    while True:
        print("(========== Menu ==========)")
        print("| 1:Total do estoque       |")
        print("| 2:Estoque Baixo          |")
        print("| 3:Adicionar estoque      |")
        print("| 4:Valor total no estoque |")
        print("(==========================)")
        try:
            escolhar = int(input("Qual será sua escolhar:"))
            print("\n")
            if escolhar == 1:
                verificar_estoque(estoque)
            elif escolhar == 2:
                baixo_estoque(estoque)
            elif escolhar == 3:
                adicionar_estoque(estoque)
            elif escolhar == 4:
                valor_total(estoque)
            else:
                print("Numero Inválido")
        except ValueError:
            print("Por favor digite numero")
        
menu(estoque)
