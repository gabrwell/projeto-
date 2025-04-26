import os
restaurantes = [{'nome': 'Pizza crazy' , 'categoria' : 'italian' , 'ativo' : True} ,   
                {'nome': 'Abacate' , 'categoria' : 'fruta' , 'ativo' : False} ,
                 {'nome': 'Carne' , 'categoria' : 'churrasco' , 'ativo' : False} ]

def definir_nome():
    print("𝑆𝑎𝑏𝑜𝑟 𝑒𝑥𝑝𝑟𝑒𝑠𝑠\n")

def exibir_menu():
    print("1. Register restaurant")
    print("2. list restaurant")
    print("3. change restaurant status ")
    print("4. leave\n")

def finalizar_app():
    subtitle("Closing program")


def voltar_menu():
    input("Press a key to return to the main menu ")
    main()

def opcao_invalida():
    print("Invalid Option!\n ")
    voltar_menu()

def subtitle(text):
    os.system('cls')
    linha = '*' (len(text))
    print(linha)
    print(text)
    print(linha)
    print()


def cadastrar_restaurante():
    subtitle("Register new restaurants")
    nome_do_restaurante = input("Enter the name of the restaurant to register: ")
    categoria = input(f"Enter the category of the restaurant {nome_do_restaurante}:  ")
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f"The name of the restaurant is {nome_do_restaurante}")
    voltar_menu()

def listar_restaurantes():
    subtitle("List new restaurants")

    print(f"{'Name of the restaurant'.ljust(20)} - {'Category'.ljust(20)} - Status ")
    for restaurant in restaurantes:
        nome_restaurant = restaurant['nome']
        categoria = restaurant['categoria']  
        ativo =  'actived' if restaurant['ativo']  else 'desactived'
        print(f"- {nome_restaurant.ljust(20)} - {categoria.ljust(20)} - {ativo}")

    voltar_menu()

def alterar_estado_restaurante():
    subtitle("Changing the status of the restaurant")
    nome_restaurant = input("Enter the name of the restaurant you want to change the status: ")
    restaurante_encontrado = False



    


    for restaurant in restaurantes:
        if nome_restaurant == restaurant['nome']:
            restaurante_encontrado = True
            restaurant['ativo'] = not restaurant['ativo']
            mensagem = f'The restaraunt {nome_restaurant} has been actived sucessuful' if restaurant['ativo'] else f'The restaurant {nome_restaurant} has been desatived sucessuful'
            print(mensagem)
    if not restaurante_encontrado:
        print("The restaurant was not found")


    voltar_menu()




def escolha_opcao():
    try:
        opcao_escolhida = int(input("Choose the option: "))


        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    definir_nome()
    exibir_menu()
    escolha_opcao()



if __name__ == '__main__':
    main()


