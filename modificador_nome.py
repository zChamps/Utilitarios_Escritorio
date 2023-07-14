def encurtador_nome():
    import os

    lista = []
    while True:
        pergunta = input("Você deseja realizar o procedimento ou sair? ")
        if pergunta == "sair":
            break
        else:
            os.system("cls")
            while True:
                nomes = input("""Digite os nomes: """).upper().split(" ")
                if "S" in nomes:
                    break
                lista.append(nomes)
            i = 0

            while i < len(lista):
                verificacao = lista[i][0] == "FRANCISCO" or lista[i][0] == "MARIA" or lista[i][0] == "JOSE" or lista[i][0] == "JOAO"
                if len(lista[i]) > 2 and len(lista[i]) < 4:
                    if verificacao:
                        i += 1
                        continue
                    lista[i].pop(1)
                elif len(lista[i]) > 3 and len(lista[i]) < 5:
                    if verificacao:
                        i += 1
                        continue        
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 4 and len(lista[i]) < 6:
                    if verificacao:
                        i += 1
                        continue
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 5 and len(lista[i]) < 7:
                    if verificacao:
                        i += 1
                        continue            
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 6 and len(lista[i]) < 8:
                    if verificacao:
                        i += 1
                        continue            
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 7 and len(lista[i]) < 9:
                    if verificacao:
                        i += 1
                        continue            
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                i += 1
            os.system("cls")
            for a in lista:
                print(" ".join(a))