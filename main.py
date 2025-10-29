listarFuncionarios = []

while True:
    print("=== MENU DE FUNCIONÁRIOS ===")
    print("1 - Cadastrar funcionários")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionários")
    print("4 - Média salarial")
    print("0 - Sair")

    menu = input("ESCOLHA OPÇÃO DESEJAZADA: ")

    ## CADASTRA FUNCIONARIO NA LISTA
    if menu == "1":
        nome = input("DIGITE O NOME DO FUNCIONARIO: ")
        salario = float(input("DIGITE O SALARIO DO FUNCIONARIO: "))
        listarFuncionarios.append({"nome": nome, "salario": salario})
        print("CADASTRO DE FUNCIONARIO REALIZADO COM SUCESSO!\n")
        print()

    ## LISTA DO FUNCIONARIOS
    elif menu == "2":
        if not listarFuncionarios:
            print("NENHUM FUNCIONARIO CADASTRADO!\n")
            print()
        else:
            print("LISTA DE FUNCIONARIOS: ")
            for f in listarFuncionarios:
                print(f"FUNCIONARIO: {f['nome']} - SALÁRIO: R${f['salario']:.2f}")

    ## BUSCA O FUNCIONARIO PELO NOME
    elif menu == "3":
        nome_busca = input("DIGITE O NOME DO FUNCIONARIO QUE QUEIRA BUSCAR: ")
        encontrado = False
        for f in listarFuncionarios:
            if f["nome"].lower() == nome_busca.lower():
                print(f"FUNCIONARIO ENCONTRADO: {f['nome']} - SALÁRIO: R${f['salario']:.2f}\n")
                print()
                encontrado = True
                break
        if not encontrado:
            print("NENHUM FUNCIONARIO ENCONTRADO!\n")
            print()

    ## MEDIA SALARIAL
    elif menu == "4":
        if not listarFuncionarios:
            print("NÃO HÁ NENHUM FUNCIONARIO REGISTRADO NO SISTEMA!\n")
            print()
        else:
            soma = 0
            i = 0
            for f in listarFuncionarios:
                soma += f["salario"]
                i += 1
            media = soma / i
            print(f"MEDIA SALARIAL: R${media:.2f}\n")
            print()

    ## OPCAO DE SAIDA
    elif menu == "0":
        print("ADEUS...")
        break
    else:
        print("OPÇÃO INVALIDA! TENTE NOVAMENTE!\n")
        print()