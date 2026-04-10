tarefas = []

#if + if + if → pode executar vários
#if + elif → só executa um

def mostrar_tarefas():
    if not tarefas:
            print("\n A lista de tarefas está vazia, digite outro numero.")
    else:
            mostrar_tarefas()
    print("Sua lista de tarefas esta logo abaixo! ")
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"{numero}. {tarefa}")


while True:
    
    try:
        opcao = int(input("\n 1. Para adicionar uma tarefa. \n 2. Para visualizar tarefas. \n 3. Para finalizar. \n 4. Remover tarefa. \n- "))
    except ValueError:
        print("Comando inválido! Digite apenas números.")
        continue

    if opcao not in (1, 2, 3, 4):
        print("Comando invalido, por favor siga apenas os numeros descritos no programa.")
        continue
               
    if opcao == 1:
        adicionar = input("\n Adicione aqui uma tarefa a sua lista: ")
        tarefas.append(adicionar)
        print("\nTarefa adicionada com sucesso! ")
    
    elif opcao == 2:
        
            mostrar_tarefas()
            
    elif opcao == 3:
        print("\n Programa finalizado.")
        break

    elif opcao == 4:
        try:
            if not tarefas: 
                print("Não há tarefas para remover.")
                continue

            mostrar_tarefas()

            removendo = int(input("Digite o número da tarefa que deseja remover: "))

            if removendo < 1 or removendo > len(tarefas):
                print("Número inválido.")
                continue

            tarefas.pop(removendo - 1)
            print("Tarefa removida com sucesso!")

        except ValueError:
            print("Digite apenas números.")