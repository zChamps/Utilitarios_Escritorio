def separador_nome_mat():

    lst_mat = []
    lst_nm = []
    lista = []

    while True:
        pergunta = input("Você deseja realizar o processo ou sair? ").lower()
        if pergunta == "sair":
              break
        else:
            while True:
                texto = input("Digite a string a ser separada: ")
                if texto.upper() == "S":
                    break
                lista.append(texto)
            for texto in lista:
                partes = texto.split("(", maxsplit=2)       
                lst_nm.append(partes[0])
                lst_mat.append(partes[1].replace(")", ""))
            
            for i in lst_mat:
                        print(i)
            for i in lst_nm:
                        print(i)
            
        
