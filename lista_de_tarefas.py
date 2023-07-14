

def lista_tarefas():
    import json
    import os

    def ler(tarefas, caminho_arquivo):
        dados = tarefas
        try:
            with open(caminho_arquivo, "r", encoding="utf8") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print("ARQUIVO NÃO EXISTE")
            salvar(tarefas, caminho_arquivo)
        return dados


    def salvar(tarefas, caminho_arquivo):
        with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2,
            ensure_ascii=False)
        return dados

    CAMINHO_ARQUIVO =  "lista_tarefas.json"
    lista_tarefas = ler([], CAMINHO_ARQUIVO)
    lista_desfazer = []

    while True:

        comando = input("Comandos: Listar, Desfazer, Refazer, Excluir ou Sair.\nDigite uma \
tarefa ou comando: ").lower()
        salvar(lista_tarefas, CAMINHO_ARQUIVO)

        if comando == "listar":
            os.system('cls')
            if len(lista_tarefas) == 0:
                os.system('cls')
                print("Não existe nenhum item na lista.\n\n")
                continue
            for i, item in enumerate(lista_tarefas):
                    print(f"{i} - {item}")
            continue
        elif comando == "desfazer":
            os.system('cls')
            if len(lista_tarefas) ==0:
                print("Ainda não existe nenhum item na lista para ser desfeito.\n\n")
                continue   
            lista_desfazer.append(lista_tarefas[-1])
            lista_tarefas.pop()
            if len(lista_tarefas) == 0:
                continue
            print(",\n".join(lista_tarefas))



def lista_tarefas():
    import json
    import os

    def ler(tarefas, caminho_arquivo):
        dados = tarefas
        try:
            with open(caminho_arquivo, "r", encoding="utf8") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            print("Arquivo não existe, criando um agora!")
            salvar(tarefas, caminho_arquivo)
        return dados


    def salvar(tarefas, caminho_arquivo):
        with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2,
            ensure_ascii=False)
        return dados

    CAMINHO_ARQUIVO =  "lista_tarefas.json"
    lista_tarefas = ler([], CAMINHO_ARQUIVO)
    lista_desfazer = []

    while True:

        comando = input("Comandos: Listar, Desfazer, Refazer, Excluir ou Sair.\nDigite uma \
tarefa ou comando: ").lower()
        salvar(lista_tarefas, CAMINHO_ARQUIVO)

        if comando == "listar":
            os.system('cls')
            if len(lista_tarefas) == 0:
                os.system('cls')
                print("Não existe nenhum item na lista.\n\n")
                continue
            for i, item in enumerate(lista_tarefas):
                    print(f"{i} - {item}")
            continue
        elif comando == "desfazer":
            os.system('cls')
            if len(lista_tarefas) ==0:
                print("Ainda não existe nenhum item na lista para ser desfeito.\n\n")
                continue   
            lista_desfazer.append(lista_tarefas[-1])
            lista_tarefas.pop()
            if len(lista_tarefas) == 0:
                continue
            print(",\n".join(lista_tarefas))
            continue
        elif comando == "refazer":
            os.system('cls')
            if len(lista_desfazer) ==0:
                print("Não existem ações para serem refeitas.\n\n")
                continue
            os.system('cls')
            lista_tarefas.append(lista_desfazer[-1])
            lista_desfazer.pop()
            print(",\n".join(lista_tarefas))
            continue
        elif comando == "excluir":
            os.system('cls')
            try:
                for i, item in enumerate(lista_tarefas):
                    print(f"{i} - {item}")
                item_excluido = int(input("Digite o número do item a ser excluido: "))
                excluir = lista_tarefas.pop(item_excluido)
                print(f"O item >{excluir}< foi excluido.")
                continue
            except ValueError:
                print("Digite uma opção válida!")
                continue
            except IndexError:
                print("Digite uma opção dentre as apresentadas!")
                continue
        elif comando == "sair":
            os.system('cls')
            print("Lista atual: "), print(", ".join(lista_tarefas))
            print("Lista finalizada.")
            break
        else:
            os.system('cls')
            lista_tarefas.append(comando)       
            for i, item in enumerate(lista_tarefas):
                    print(f"{i} - {item}")
        