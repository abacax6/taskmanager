# Data structure / Estrutura de dados
# task = {"id": int, "title": str, "description": str, "status": str}
task_list = {}
valid_status = ["to do", "in progress", "completed"]
next_id = 1

#Basic features / Funcionalidades básicas

#Criar task [C]
def create_task(title, description):
    global next_id

    task_list[next_id] = {
        "id": next_id,
        "title": title,
        "description": description,
        "status": 'to do'
    }
    next_id += 1 #Incrementamos o ID global manualmente

#Listar tasks [R]
def list_tasks():
    if not task_list: #Caso de não haver tarefas (dicionario vazio)
        print("\n**** LISTA DE TAREFAS ****")
        print("Nenhuma tarefa cadastrada")
        return

    print("\n**** LISTA DE TAREFAS ****")
    for task in task_list.values():
        print(f"[{task['id']}] {task['title']}")
        print(f"Descrição: {task['description']}")
        print(f"Status: {task['status']}")
        print("*" * 30)

#Update task [U]
def update_task(task_id, new_status):
    if task_id not in task_list:
        print("Tarefa não encontrada.")
        return

    if new_status not in valid_status:
        print("Status inválido.")
        print(f"Use um destes: {', '.join(valid_status)}")
        return

    task_list[task_id]["status"] = new_status
    print("Status atualizado.")

#Delete task [D]
def delete_task(task_id):
    if task_id not in task_list:
        print("Tarefa não encontrada.")
        return
    
    confirm = input(f"Tem certeza que deseja deletar a tarefa {task_id}? (s/n): ").lower()

    if confirm == "s":
        del task_list[task_id]
        print("Tarefa deletada.")
    else:
        print("Operação cancelada.")
        
#Func para exibir o menu do CRUD
def menu(): 
    print("\n **** TASK MANAGER ****")
    print("1 - Criar tarefa [C]") #Create
    print("2 - Listar tarefas [R]") #Read
    print("3 - Atualizar status [U]") #Update
    print("4 - Deletar tarefa [D]") #Delete
    print("0 - Sair")

#Start / Início 
while True:
    menu()
    option = input("Escolha uma opção: ")

    if option == "1":
        title = input("Título: ")
        description = input("Descrição: ")
        create_task(title, description)

    elif option == "2":
        list_tasks()

    elif option == "3":
        try:
            task_id = int(input("ID da tarefa: "))
            status = input("Novo status: ").lower()

            update_task(task_id, status)

        except ValueError:
            print("ID inválido.")

    elif option == "4":
        try:
            task_id = int(input("ID da tarefa: "))
            delete_task(task_id)
        except ValueError:
            print("ID inválido.")

    elif option == "0":
        print("*Saindo...")
        break

    else:
        print("*Opção inválida.")