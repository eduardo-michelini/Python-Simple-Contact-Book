contatos = {}
print("Agenda de Contatos Simples")

nome = input("Digite o seu nome usuário: ").upper()

while True:
    print("\nOpções")
    print("1 - Adicionar Contato")
    print("\n2 - Ver Lista de Contatos")
    print("\n3 - Buscar Contato por Nome")
    print("\n4 - Excluir Contatos")
    print("\n5 - Sair \n")
    
    opcao_usuario = int(input(f"Digite uma opção usuário {nome}: "))
    
    if opcao_usuario == 1:
        novo_contato = input(f"Digite o nome do novo contato usuário {nome}: ").upper()
        novo_numero = input(f"Digite o número do novo contato usuário {nome} (Adicione no formato Completo para discagem, ex : +55 11 98765-4321, digite com os espaços e caracteres): ")
        
        if len(novo_numero) == 17:
            contatos[novo_contato] = {
                "Nome": novo_contato,
                "Telefone": novo_numero
            }
            print(f"Usuário {nome}, o contato {novo_contato} foi adicionado com sucesso!")
            
        else:
            print(f"Número inválido usuário {nome}, tente novamente")
        
    elif opcao_usuario == 2:
        print("Lista de Contatos")
        if not contatos:
            print(f"Usuário {nome}, você ainda não possue contatos!")
        else:
            for chave, dados in contatos.items():
                print(f"Nome: {dados['Nome']} - Telefone: {dados['Telefone']}")
            
    elif opcao_usuario == 3:
        nome_procurar = input(f"Usuário {nome}, digite o nome que você deseja procurar: ").upper()
        
        if nome_procurar in contatos:
            print(f"Usuário {nome}, o contato {nome_procurar} foi encontrado!")
            print(f"Telefone: {contatos[nome_procurar]['Telefone']}")
        else:
            print(f"Usuário {nome}, o contato {nome_procurar} não foi encontrado!")
            
    elif opcao_usuario == 4:
        nome_remover = input(f"Usuário {nome}, digite o nome que você deseja remover da sua lista de contatos: ").upper()
        
        if nome_remover in contatos:
            print(f"Usuário {nome}, o contato {nome_remover} foi removido!")
            del contatos[nome_remover]

        else:
            print(f"Usuário {nome}, o contato {nome_remover} não foi encontrado!")
    
    elif opcao_usuario == 5:
        print(f"Usuário {nome}, obrigado por utilizar nossa Agenda de Contatos Simples, espero que tenha gostado!")
        break
    
    else:
        print(f"Opção inválida usuário {nome}, tente novamente!")