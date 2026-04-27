# Importação de biblioteca os para melhorar a estética do menu CLI com o comando de limpar terminal (27/04/2026)
import os

#Func para limpar o terminal usando o import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Data structure / Estrutura de dados
# task = {"id": int, "title": str, "description": str, "status": str}

# Global variables / Variáveis globais
TASK_LIST = {}
VALID_STATUS = ["to do", "in progress", "completed"]
NEXT_ID = 0

#Func para a opção de voltar ao menu principal
def back():
    input("\nPressione qualquer tecla para continuar...")

#Basic features / Funcionalidades básicas

#Criar task [C]
def create_task(title, description):
    global NEXT_ID

    TASK_LIST[NEXT_ID] = {
        "id": NEXT_ID,
        "title": title,
        "description": description,
        "status": 'to do' #Já inicializa a nova tarefa com o status "to do"
    }
    NEXT_ID += 1 #Incrementamos o ID global manualmente
    print("Tarefa adicionada com sucesso.\n")
    print("*" * 30)
    back()


#Listar tasks [R]
def list_tasks():
    print("****** LISTA DE TAREFAS ******")
    print("*" * 30)
    if not TASK_LIST: #Caso de não haver tarefas (dicionario vazio)
        print("Nenhuma tarefa cadastrada.\n")

    for task in TASK_LIST.values(): #Listar cada task existente
        print(f"\n[{task['id']}] {task['title']}")
        print(f"Descrição: {task['description']}")
        print(f"Status: {task['status']}\n")
        print("*" * 30)
    back()
    

#Update task [U]
def update_task(task_id, new_status):
    if task_id not in TASK_LIST:
        print("ID inválido, tarefa não encontrada.")
        
    elif new_status not in VALID_STATUS:
        print("Status inválido.")
        print(f"Use um destes: {', '.join(VALID_STATUS)}") #Método .join() servindo para CONCATENAR as strings contidas na lista dos status válidos
        
    else:
        TASK_LIST[task_id]["status"] = new_status
        print("Status atualizado.")
        
    print("\n" + "*" * 30)
    back()


#Delete task [D]
def delete_task(task_id):
    if task_id not in TASK_LIST:
        print("Tarefa não encontrada.")
        print("\n" + "*" * 30)
        return back()
    
    confirm = input(f"Tem certeza que deseja deletar a tarefa {task_id}? (s/n): ").lower()
    if confirm == "s":
        del TASK_LIST[task_id]
        print("Tarefa deletada.")
        print("\n" + "*" * 30)
    else:
        print("Operação cancelada.")
        print("\n" + "*" * 30)
    back()


#Func para exibir o menu do CRUD
def menu(): 
    print("******** TASK MANAGER ********")
    print("*" * 30 + "\n")
    print("1 - Criar tarefa           [C]") #Create
    print("2 - Listar tarefas         [R]") #Read
    print("3 - Atualizar status       [U]") #Update
    print("4 - Deletar tarefa         [D]") #Delete
    print("0 - Sair\n")
    print("*" * 30)


#Start / Início 
def main():
    while True:
        clear()
        menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            clear()
            print("******** NOVA TAREFA ********")
            print("*" * 30 + "\n")
            title = input("Título: ")
            description = input("Descrição: ")
            create_task(title, description)

        elif option == "2":
            clear()
            list_tasks()

        elif option == "3":
            clear()
            print("****** ATUALIZAR STATUS ******")
            print("*" * 30 + "\n")
            try:
                task_id = int(input("ID da tarefa: "))
                status = input("Novo status: ").lower()

                update_task(task_id, status)

            except ValueError:
                print("ID inválido.")
                back()

        elif option == "4":
            clear()
            print("***** EXCLUIR TAREFA *****")
            print("*" * 30 + "\n")
            try:
                task_id = int(input("ID da tarefa: "))
                delete_task(task_id)
            except ValueError:
                print("ID inválido.")
                back()

        elif option == "0":
            print("*Saindo...")
            break

        else:
            print("*Opção inválida.")


#Chamada da função principal
main()