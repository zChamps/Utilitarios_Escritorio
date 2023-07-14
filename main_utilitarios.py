import lista_de_tarefas
import modificador_nome
import pontos_cpf
import separador_nome_matricula
import simplificador_escala
import os

while True:
    os.system("cls")
    print("Utilitários Atendimento em Geral: \n1 - Lista de Tarefas \n2 - Alteração de CPF\
\n\n Utilitários para Crachá: \n3 - Simplificador de Nomes \n4 - Simplificador de Escala\
\n5 - Separador Nome/Matricula \n\n6 - Sair")
    pergunta = input("\nDigite a opção desejada: ")

    if pergunta == "1":
        os.system("cls")
        lista_de_tarefas.lista_tarefas()

    elif pergunta == "2":
        os.system("cls")
        pontos_cpf.alterador_CPF()

    elif pergunta == "3":
        os.system("cls")       
        modificador_nome.encurtador_nome()

    elif pergunta == "4":
        os.system("cls")
        simplificador_escala.escalas()

    elif pergunta == "5":
        os.system("cls")
        separador_nome_matricula.separador_nome_mat()

    elif pergunta == "6":
        break

    else:
        os.system("cls")
        print("Digite uma opção válida!")
        continue

    