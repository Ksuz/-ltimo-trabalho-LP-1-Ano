a = 1
i = 0
qtcadastro = 1
nam = input("Digite o nome do seu arquivo: ")
arquivo = open(nam + '.txt', 'a', )
arquivo.close()
while a != 5:
    print("     |Menu| ")
    print(" ---------------")
    print(' |1 - Cadastrar| \n |2 - Ler      | \n |3 - Deletar  | \n |4 - Atualizar| \n |5 - Sair     |')
    print(" ---------------")
    op = int(input("\n • Escolha algum dos itens acima: "))
    if op == 1:
        b = 0
        while b == 0:
            print(" |Menu de cadastro| ")
            print(" •Nome\n", "•Sobrenome\n", "•Idade\n", "•Cidade\n", "•Número da casa\n", "•Telefone")
            qtcadastro: int = int(input(" •Quantidade de cadastros que deseja fazer: "))
            i = 0
            while i < qtcadastro:
                arquivo = open(nam + '.txt', 'a', )
                nome = (input(" •Nome: "))
                sobrenome = (input(" •Sobrenome: "))
                idade = (input(" •Idade: "))
                cpf = (input(" •Cidade: "))
                cidade = (input(" •N° da casa: "))
                i = i + 1
                arquivo.writelines("-----------------------------------------")
                arquivo.writelines("\nnomes:")
                arquivo.writelines(nome)
                arquivo.writelines("\nsobrenomes:")
                arquivo.writelines(sobrenome)
                arquivo.write("\nidades:")
                arquivo.writelines(idade)
                arquivo.write("\ncpfs:")
                arquivo.writelines(cpf)
                arquivo.write("\ncidades:")
                arquivo.writelines(cidade)
                arquivo.writelines("\n-----------------------------------------")
                arquivo.close()
                yn = int(input(" •Deseja concluir o cadastro? \n 1-Sim\n 2-Não\n "))
            if yn == 1:
                b = 1
            elif yn == 2:
                b = 0
    i = 0
    if op == 2:
        arquivo = open(nam + '.txt', 'r')
        string = arquivo.read()
        print(string)
        arquivo.close()

    elif op == 3:
        arquivo = open(nam + '.txt', 'r')
        string2 = arquivo.readlines()
        if len(string2) > 1:
            arquivo = open(nam + '.txt', 'w', )
            arquivo.write('')
            print('DELETAR \n')
            arquivo.close()
        else:
            print("Sem cadastros")
        arquivo.close()
    elif op == 4:
        arquivo = open(nam + '.txt', 'r')
        string3 = arquivo.readlines()
        if len(string3) > 1:
            b = 0
            while b == 0:
                qtcadastro: int = int(input("Quantos deseja fazer?"))
                i = 0
                while i < qtcadastro:
                    arquivo = open(nam + '.txt', 'w', )
                    nome = (input(" •Nome: "))
                    sobrenome = (input(" •Sobrenome: "))
                    idade = (input(" •Idade: "))
                    cpf = (input(" •Cidade: "))
                    cidade = (input(" •N° da casa: "))
                    i = i + 1
                    arquivo.writelines("\n-----------------------------------------")
                    arquivo.writelines("\nnomes:")
                    arquivo.writelines(nome)
                    arquivo.writelines("\nsobrenomes:")
                    arquivo.writelines(sobrenome)
                    arquivo.write("\nidades:")
                    arquivo.writelines(idade)
                    arquivo.write("\ncpfs:")
                    arquivo.writelines(cpf)
                    arquivo.write("\ncidades:")
                    arquivo.writelines(cidade)
                    arquivo.writelines("\-----------------------------------------")
                    arquivo.close()
                    i = i + 1
                    yn = int(input(" •Deseja concluir o re-cadastro? \n 1-Sim\n 2-Não\n "))
                    if yn == 1:
                        b = 1
                    elif yn == 2:
                        b = 0
        else:
            print("Sem cadastros")
        arquivo.close()
    if op == 5:
        quit = int(input(" 1-Sair\n 2-Não sair  \n "))
        if quit == 1:
            a = 5
        elif quit == 2:
            a = 1
