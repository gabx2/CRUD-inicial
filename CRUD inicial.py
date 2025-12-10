import json

todos_alunos = {}
todos_professores = {}
todos_disciplinas = {}
todos_turmas = {}
todos_matriculas = {}
def mostrar_primeiro_menu ():
    print ("----MENU PRINCIPAL-----\n(1) Gerenciar Estudantes\n(2) Gerenciar Professores\n(3) Gerenciar Disciplinas\n"
              "(4) Gerenciar Turmas\n(5) Gerenciar Matriculas\n(9) Sair\n")
    return input("Escolha uma das opções acima:").lower()
def mostrar_segundo_menu (tipo_menu):
    print (F"\n---- MENU {tipo_menu}----\n(1) Incluir\n(2) Listar\n(3) Atualizar\n"
             "(4) Excluir\n(5) Salvar\n(6) Carregar\n(9) Voltar ao menu anterior")
    return input("\nEscolha uma das alternativas acima:").lower()
def incluir_professor_e_aluno(dicionario, categoria):
    while True:
        chave = input(f"\nInforme a {'matrícula' if categoria=='Aluno' else 'código'} do {categoria.lower()}: ")
        if chave in dicionario:
            while True:
                atualizar = input(f"{categoria} já cadastrado(a). Deseja atualizar o cadastro? (s/n) ").lower()
                if atualizar in ['s', 'n']:
                    break
                else:
                    print("Digite uma opção válida!")
            if atualizar == 'n':
                return

        nome = input(f"\nInforme o nome do {categoria.lower()}: ")
        cpf = input(f"Informe o CPF do {categoria.lower()}: ")
        dicionario[chave] = {"nome": nome, "cpf": cpf}
        while True:
            mais = input("\nDeseja cadastrar mais alguém? (s/n) ").lower()
            if mais == "n":
                return
            elif mais == 's':
                break
            else:
                continue
def incluir_disciplina(dicionario, categoria):
    while True:
        chave = input(f"\nInforme o código da disciplina que deseja incluir:")
        if chave in dicionario:
            while True:
                atualizar = input(f"{categoria} já cadastrado(a). Deseja atualizar o cadastro? (s/n) ").lower()
                if atualizar in ['s', 'n']:
                    break
                else:
                    print("Digite uma opção válida!")
            if atualizar == 'n':
                return

        nome_disciplina = input(f"\nInforme o Código da {categoria.lower()}: ")
        dicionario[chave] = {"nome": nome_disciplina}
        while True:
            mais = input("\nDeseja cadastrar mais alguém? (s/n) ").lower()
            if mais == "n":
                return
            elif mais == 's':
                break
            else:
                continue
def incluir_turma(dicionario, categoria):
    while True:
        chave = input(f"\nInforme o código da turma que deseja incluir:")
        if chave in dicionario:
            while True:
                atualizar = input(f"{categoria} já cadastrado(a). Deseja atualizar o cadastro? (s/n) ").lower()
                if atualizar in ['s', 'n']:
                    break
                else:
                    print("Digite uma opção válida!")
            if atualizar == 'n':
                return

        codigo_professor = input(f"\nInforme o Código do Professor: ")
        codigo_disciplina = input(f"\nInforme o Código do disciplina   : ")
        dicionario[chave] = {"codigo professor": codigo_professor, "codigo disciplina": codigo_disciplina}
        while True:
            mais = input("\nDeseja cadastrar mais alguém? (s/n) ").lower()
            if mais == "n":
                return
            elif mais == 's':
                break
            else:
                continue
def incluir_matriculas(dicionario, categoria):
    while True:
        chave = input(f"\nInforme o código da matricula que deseja incluir:")
        if chave in dicionario:
            while True:
                atualizar = input(f"{categoria} já cadastrado(a). Deseja atualizar o cadastro? (s/n) ").lower()
                if atualizar in ['s', 'n']:
                    break
                else:
                    print("Digite uma opção válida!")
            if atualizar == 'n':
                return

        codigo_estudante = input(f"\nInforme o Código do estudante: ")
        dicionario[chave] = {"codigo estudante": codigo_estudante}

        while True:
            mais = input("\nDeseja cadastrar mais alguém? (s/n) ").lower()
            if mais == "n":
                return
            elif mais == 's':
                break
            else:
                print("Digite uma opção válida!")
                continue
def listar_item(dicionario, categoria):
    if len(dicionario) == 0:
        print(f"\nSem {categoria.lower()} cadastrados(as)")
        return
    else:
        if categoria == 'Alunos' or categoria == 'Professores':
            print(f"\n{categoria} cadastrados:\n")
            for chave, valor in sorted(dicionario.items()):
                print(f"--------\n{'Matrícula' if categoria=='Alunos' else 'Código'}: {chave}\nNome: {valor['nome']}\nCPF: {valor['cpf']}")
        elif categoria == 'Disciplinas':
            for chave, valor in sorted(dicionario.items()):
                print(f"--------\nCódigo da disciplina: {chave}\nNome da disciplina: {valor['nome']}")
        elif categoria == 'Turmas':
            for chave, valor in sorted(dicionario.items()):
                print(f"--------\nCódigo Turma: {chave}\nCódigo Professor: {valor['codigo professor']}\nCódigo da disciplina: {valor['codigo disciplina']}")
        elif categoria == 'Matriculas':
            for chave, valor in sorted(dicionario.items()):
                print(f"--------\nCódigo da Matricula: {chave}\nCódigo do aluno: {valor['codigo estudante']}")

def atualizar_dados (dicionario, categoria):
    if len(dicionario) == 0:
        print(f"\nSem {categoria} cadastrados(as)")
    else:
        while True:
            chave = input("\nQual código/matrícula deseja atualizar?\n")
            if chave in dicionario:
                dado_atualizar = dicionario[chave]
                if categoria == 'Alunos' or categoria == 'Professores':
                    print(f"--------\nCódigo: {chave}\nNome: {dado_atualizar['nome']}\nCPF: {dado_atualizar['cpf']}")
                elif categoria == 'Disciplinas':
                    print(f"--------\nCódigo da disciplina: {chave}\nNome da disciplina: {dado_atualizar['nome']}")
                elif categoria == 'Turmas':
                    print(f"--------\nCódigo Turma: {chave}\nCódigo Professor: {dado_atualizar['codigo professor']}\nCódigo da disciplina: {dado_atualizar['codigo disciplina']}")
                elif categoria == 'Matriculas':
                    print(f"--------\nCódigo da Matricula: {chave}\nCódigo do aluno: {dado_atualizar['codigo estudante']}")

                atualizar_confirma = input("Deseja atualizar o cadastro acima? (s/n): ").lower()
                if atualizar_confirma == "n":
                    print("Atualização Cancelada")
                    break

                elif atualizar_confirma == "s":
                    if categoria == 'Alunos' or categoria == 'Professores':
                        print("\nMENU ATUALIZAR\n1 - Atualizar código/matrícula\n2 - Atualizar nome\n3 - Atualizar CPF\n9 - Sair")
                    elif categoria == 'Disciplinas':
                        print("\nMENU ATUALIZAR\n1 - Atualizar Código da Disciplina\n2 - Atualizar nome da disciplina\n9 - Sair")
                    elif categoria == 'Turmas':
                        print("\nMENU ATUALIZAR\n1 - Atualizar Código da Turma\n2 - Atualizar código do professor\n3 - Atualizar código da disciplina\n9 - Sair")
                    elif categoria == 'Matriculas':
                        print("\nMENU ATUALIZAR\n1 - Atualizar Código da Matricula\n2 - Atualizar código do aluno\n9 - Sair")
                    escolha_menu_atualizar = input("Escolha uma das alternativas acima:").lower()

                    if escolha_menu_atualizar == "1":
                        novo_codigo = input(f"\nInforme código novo")
                        dicionario[novo_codigo] = dado_atualizar.copy()
                        del dicionario[chave]
                        print("\nCÓDIGO/MATRÍCULA ATUALIZADO\n")
                        break

                    elif escolha_menu_atualizar == "2":
                        if categoria == 'Alunos' or categoria == 'Professores':
                            novo_nome = input("\nInforme o nome atualizado:")
                            dado_atualizar['nome'] = novo_nome
                            print("\nNOME ATUALIZADO\n")
                            break
                        elif categoria == 'Disciplinas':
                            novo_nome_disciplina = input("\nInforme o nome atualizado:")
                            dado_atualizar['nome'] = novo_nome_disciplina
                            print("\nNOME ATUALIZADO\n")
                            break
                        elif categoria == 'Turmas':
                            novo_codigo_professor = input("\nInforme o código professor atualizado:")
                            dado_atualizar['codigo_professor'] = novo_codigo_professor
                            print ("\nCÓDIGO ATUALIZADO\n")
                            break
                        elif categoria == 'Matriculas':
                            novo_codigo_aluno = input("\nInforme o código aluno atualizado:")
                            dado_atualizar['codigo estudante'] = novo_codigo_aluno
                            print("\nCÓDIGO ATUALIZADO\n")
                            break

                    elif escolha_menu_atualizar == "3":
                        if categoria == 'Alunos' or categoria == 'Professores':
                            novo_cpf = input("\nInforme o CPF atualizado:")
                            dado_atualizar['cpf'] = novo_cpf
                            print("\nCPF ATUALIZADO\n")
                            break
                        if categoria == 'Turmas':
                            codigo_disciplina = input("\nInforme o código disciplina atualizado:")
                            dado_atualizar['codigo disciplina'] = codigo_disciplina
                            print("\nCÓDIGO ATUALIZADO\n")
                            break

                    elif escolha_menu_atualizar == "9":
                        print("\nSaindo do menu de atualização...\n")
                        break

                    else:
                        print("Opção inválida!")
                else:
                    print("Opção inválida!")
            else:
                print("Código/Matrícula não encontrado!")
def excluir_dados(dicionario, categoria):
    if len(dicionario) == 0:
        print(f"\nSem {categoria.lower()}s cadastrados(as)")
        return

    while True:
        chave_para_excluir = input(f"\nQual {categoria.lower()} deseja excluir? (Informe o código/matrícula)\n")
        if chave_para_excluir in dicionario:
            item = dicionario[chave_para_excluir]
            if categoria == 'Alunos' or categoria == 'Professores':
                print(f"--------\nCódigo/Matrícula: {chave_para_excluir}\nNome: {item['nome']}\nCPF: {item['cpf']}")
            elif categoria == 'Disciplinas':
                print(f"--------\nCódigo da disciplina: {chave_para_excluir}\nNome da disciplina: {item['nome']}")
            elif categoria == 'Turmas':
                print(f"--------\nCódigo Turma: {chave_para_excluir}\nCódigo Professor: {item['codigo professor']}\nCódigo da disciplina: {item['codigo disciplina']}")
            elif categoria == 'Matriculas':
                print(f"--------\nCódigo da Matricula: {chave_para_excluir}\nCódigo do aluno: {item['codigo estudante']}")


            confirmar = input(f"Deseja excluir o cadastro do {categoria.lower()} acima? (s/n): ").lower()

            if confirmar == "s":
                del dicionario[chave_para_excluir]
                print(f"{categoria} excluído(a) com sucesso!")
                break
            elif confirmar == "n":
                print("\nExclusão cancelada")
                continue
            else:
                print("Confirme ou cancele corretamente")
        else:
            print(f"{categoria} não encontrado(a)")
def salvar_cadastros(dicionario, nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados_existentes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        dados_existentes = {}

    dados_existentes.update(dicionario)

    for chave in list(dados_existentes):
        if chave not in dicionario:
            del dados_existentes[chave]

    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados_existentes, arquivo)

    print(f"\n{nome_arquivo.replace('.txt','')} com sucesso!")
def carregar_cadastros(dicionario, nome_arquivo, categoria):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados_salvos = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"\nNenhum arquivo de {categoria.lower()}s encontrado ou arquivo vazio!")
        return dicionario

    for chave, dados in dados_salvos.items():
        if chave in dicionario:
            print(f"\n{categoria} {chave} já existe!")
            print(f"Atual: Nome: {dicionario[chave]['nome']}, CPF: {dicionario[chave]['cpf']}")
            print(f"Salvo: Nome: {dados['nome']}, CPF: {dados['cpf']}")
            escolha = input("Deseja sobrescrever os dados atuais com os salvos? (s/n): ").lower()
            if escolha == "s":
                dicionario[chave] = dados
        else:
            dicionario[chave] = dados

    print(f"{categoria}s carregados com sucesso!")
    return dicionario

while True:
    escolha_menu1 = mostrar_primeiro_menu()
    if escolha_menu1 in ["1", "estudante"]:
        nome_escolha = "ESTUDANTES"
    elif escolha_menu1 in ["2","professores"]:
        nome_escolha = "PROFESSORES"
    elif escolha_menu1 in ["3"]:
        nome_escolha = "DISCIPLINAS"
    elif escolha_menu1 in ["4"]:
        nome_escolha = "TURMAS"
    elif escolha_menu1 in ["5"]:
        nome_escolha = "MATRICULAS"
    elif escolha_menu1 == "9":
        print("Saindo...")
        break
    else:
        print ("\nESCOLHA UMA OPÇÃO VALIDA\n")
        continue

    while True:
        escolha_menu2 = mostrar_segundo_menu(nome_escolha)

        if escolha_menu2 in ["1", "incluir"]:
            if nome_escolha == "ESTUDANTES":
                incluir_professor_e_aluno(todos_alunos,"Aluno")
            elif nome_escolha == "PROFESSORES":
                incluir_professor_e_aluno(todos_professores,"Professores")
            elif nome_escolha == "DISCIPLINAS":
                incluir_disciplina(todos_disciplinas,"Disciplinas")
            elif nome_escolha == "TURMAS":
                incluir_turma(todos_turmas, "Turmas")
            elif nome_escolha == "MATRICULAS":
                incluir_matriculas(todos_matriculas, "Matriculas")

        elif escolha_menu2 in ["2","listar"]:
            if nome_escolha == "ESTUDANTES":
                listar_item(todos_alunos, "Alunos")
            elif nome_escolha == "PROFESSORES":
                listar_item(todos_professores, "Professores")
            elif nome_escolha == "DISCIPLINAS":
                listar_item(todos_disciplinas, "Disciplinas")
            elif nome_escolha == "TURMAS":
                listar_item(todos_turmas, "Turmas")
            elif nome_escolha == "MATRICULAS":
                listar_item(todos_matriculas, "Matriculas")

        elif escolha_menu2 in ["3"]:
            if nome_escolha == "ESTUDANTES":
                atualizar_dados(todos_alunos, "Alunos")
            elif nome_escolha == "PROFESSORES":
                atualizar_dados(todos_professores, "Professores")
            elif nome_escolha == "DISCIPLINAS":
                atualizar_dados(todos_disciplinas, "Disciplinas")
            elif nome_escolha == "TURMAS":
                atualizar_dados(todos_turmas, "Turmas")
            elif nome_escolha == "MATRICULAS":
                atualizar_dados(todos_matriculas, "Matriculas")

        elif escolha_menu2 in ["4"]:
            if nome_escolha == "ESTUDANTES":
                excluir_dados(todos_alunos,"Alunos")
            elif nome_escolha == "PROFESSORES":
                excluir_dados(todos_professores,"Professores")
            elif nome_escolha == "DISCIPLINAS":
                excluir_dados(todos_disciplinas,"Disciplinas")
            elif nome_escolha == "TURMAS":
                excluir_dados(todos_turmas, "Turmas")
            elif nome_escolha == "MATRICULAS":
                excluir_dados(todos_matriculas, "Matriculas")

        elif escolha_menu2 in ["5"]:
            if nome_escolha == "ESTUDANTES":
                salvar_cadastros(todos_alunos,"Alunos salvos.txt")
            elif nome_escolha == "PROFESSORES":
                salvar_cadastros(todos_professores, "Professores salvos.txt")
            elif nome_escolha == "DISCIPLINAS":
                salvar_cadastros(todos_disciplinas, "Disciplinas salvas.txt")
            elif nome_escolha == "TURMAS":
                salvar_cadastros(todos_turmas, "Turmas salvas.txt")
            elif nome_escolha == "MATRICULAS":
                salvar_cadastros(todos_matriculas, "Matriculas salvas.txt")

        elif escolha_menu2 in ["6"]:
            if nome_escolha == "ESTUDANTES":
                carregar_cadastros(todos_alunos, "Alunos salvos.txt", "Alunos")
            elif nome_escolha == "PROFESSORES":
                carregar_cadastros(todos_professores, "Professores salvos.txt", "Professores")
            elif nome_escolha == "DISCIPLINAS":
                carregar_cadastros(todos_disciplinas, "Disciplinas salvas.txt", "Disciplinas")
            elif nome_escolha == "TURMAS":
                carregar_cadastros(todos_turmas, "Turmas salvas.txt", "Turmas")
            elif nome_escolha == "MATRICULAS":
                carregar_cadastros(todos_matriculas, "Matriculas salvas.txt", "Matriculas")

        elif escolha_menu2 in ["9"]:
            print("\nVOLTANDO AO MENU ANTERIOR\n")
            break
        else:
            print("\nESCOLHA UMA OPÇÃO VALIDA\n") #teste