def alterador_CPF():

    import os

    def cpf():
        while True:
            pergunta1 = input("Olá! Você deseja Incluir ou Excluir os pontos do CPF? ").lower()
            if pergunta1 == "sair":
                break
            if pergunta1 == "i" or pergunta1 == "incluir" or pergunta1 == "inserir":
                cpf_sem_pontos = input("Digite o número do CPF abaixo:\n")
                cpf_com_pontos = "{}.{}.{}-{}".format(cpf_sem_pontos[0:3], cpf_sem_pontos[3:6], cpf_sem_pontos[6:9], cpf_sem_pontos[9:])
                os.system("cls")
                print(f"Segue CPF com os pontos:\n{cpf_com_pontos}"  )  

            elif pergunta1 == "e" or pergunta1 == "excluir":
                cpf_com_pontos = input("Digite o número do CPF abaixo:\n")
                cpf_sem_pontos = cpf_com_pontos.replace(".", "").replace("-", "").replace(",", "").replace(" ", "")
                os.system("cls")
                print(f"Segue CPF sem caracteres especiais:\n{cpf_sem_pontos}")

            else:
                os.system("cls")
                print("Digite uma opção válida!")
                continue

    cpf()