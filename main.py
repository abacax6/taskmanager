# Importação de biblioteca os para melhorar a estética do menu CLI com o comando de limpar terminal (27/04/2026)
import os

# Importação direta de função autoral do nosso amigo Hebert https://github.com/pedrohebert/curso_backend/blob/main/testes/cores.py
def color(r:int = 0, g: int = 0, b:int = 0,*, fundo = False, reset= False):
    if reset: return f"\033[0m"
    plano = 38 if not fundo else 48
    return f"\033[{plano};2;{r};{g};{b}m"

# Constantes para personalização de cores
C_CREATETASK = color(45,90,245)
C_LISTTASK = color(65,105,225)
C_UPDATETASK = color(30,144,255)
C_DELETETASK = color(0,191,255)

BOLD = "\033[1m" # Negrito / BOLD
PINK_FELPS = color(254,56,103,)
RED = color(255,0,0)
GREEN = color(0,255,0)
BLUE = color(0,0,255)
CYAN = color(0,255,255)
YELLOW = color(255,255,0)
CRESET = color(reset = True)

# Data structure / Estrutura de dados
# task = {"id": int, "title": str, "description": str, "status": str}
# Global variables / Variáveis globais
TASK_LIST = {}
VALID_STATUS = ["to do", "in progress", "completed"] # Lista dos status possíveis
NEXT_ID = 0

#FUNCS AUXILIARES
#Func para limpar o terminal usando o import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#Func para a opção de voltar ao menu principal
def back():
    #import de getpass() para input oculto
    from getpass import getpass
    getpass(f"\n{BOLD}Pressione ENTER para continuar...")

#Basic features / Funcionalidades básicas
#Criar task [C]
def create_task(title, description):
    global NEXT_ID #Global para considerar a variável que já existe fora do escopo da função

    TASK_LIST[NEXT_ID] = {
        "id": NEXT_ID,
        "title": title,
        "description": description,
        "status": 'to do' #Já inicializa a nova tarefa com o status "to do"
    }
    NEXT_ID += 1 #Incrementamos o ID global manualmente
    print(f"{BOLD}{GREEN}Tarefa adicionada com sucesso.{CRESET}\n")
    print("*" * 30)
    back()


#Listar tasks [R]
def list_tasks():
    print(f"****** {BOLD}{C_LISTTASK}LISTA DE TAREFAS{CRESET} ******")
    print("*" * 30)
    if not TASK_LIST: #Caso de não haver tarefas (dicionario vazio)
        print("Nenhuma tarefa cadastrada.\n")

    for task in TASK_LIST.values(): #Listar cada task existente
        print(f"\n{BOLD}ID:{CRESET} [{CYAN}{task['id']}{CRESET}]")
        print(f"{BOLD}Título:{CRESET} {PINK_FELPS}{task['title']}{CRESET}")
        print(f"{BOLD}Descrição:{CRESET} {task['description']}")
        print(f"{BOLD}Status: {CYAN}{task['status']}{CRESET}\n")
        print("*" * 30)
    back()
    

#Update task [U]
def update_task(task_id, new_status):
    if task_id not in TASK_LIST:
        print(f"{BOLD}{RED}ID inválido, tarefa não encontrada.{CRESET}")
        
    elif new_status not in VALID_STATUS:
        print(f"{BOLD}{RED}Status inválido.{CRESET}")
        print(f"{BOLD}Use um destes: {CRESET}{CYAN}{'| '.join(VALID_STATUS)}{CRESET}") #Método .join() servindo para CONCATENAR as strings contidas na lista dos status válidos, com ', ' sendo o separador
        
    else:
        TASK_LIST[task_id]["status"] = new_status
        print(f"{BOLD}{GREEN}Status atualizado.{CRESET}")
        
    print("\n" + "*" * 30)
    back()


#Delete task [D]
def delete_task(task_id):
    if task_id not in TASK_LIST:
        print(f"{BOLD}{RED}Tarefa não encontrada.{CRESET}")
        print("\n" + "*" * 30)
        return back()
    
    confirm = input(f"{BOLD}Tem certeza que deseja deletar a tarefa de id {CYAN}{task_id}{CRESET}{BOLD} ? (s/n): {CRESET}").lower()
    if confirm == "s":
        del TASK_LIST[task_id]
        print(f"{BOLD}{GREEN}Tarefa deletada com sucesso.{CRESET}")
        print("\n" + "*" * 30)
    else:
        print(f"{BOLD}Operação cancelada.")
        print("\n" + "*" * 30)
    back()


#Func para exibir o menu do CRUD
def menu(): 
    print(f"******** {BOLD}{PINK_FELPS}TASK MANAGER{CRESET} ********")
    print("*" * 30 + "\n")
    print(f"{BOLD}1 - Criar tarefa           {C_CREATETASK}[C]{CRESET}") #Create
    print(f"{BOLD}2 - Listar tarefas         {C_LISTTASK}[R]{CRESET}") #Read
    print(f"{BOLD}3 - Atualizar status       {C_UPDATETASK}[U]{CRESET}") #Update
    print(f"{BOLD}4 - Deletar tarefa         {C_DELETETASK}[D]{CRESET}") #Delete
    print(f"{BOLD}0 - Sair{CRESET}\n")
    print("*" * 30)


#Start / Início 
def main():
    while True:
        clear()
        menu()
        option = input(f"\n{BOLD}@ - Escolha uma opção: {CRESET}")

        if option == "1":
            clear()
            print(f"******** {BOLD}{C_CREATETASK}NOVA  TAREFA{CRESET} ********")
            print("*" * 30 + "\n")
            title = input(f"{BOLD}Título: {CRESET}")
            description = input(f"{BOLD}Descrição: {CRESET}")
            create_task(title, description)

        elif option == "2":
            clear()
            list_tasks()

        elif option == "3":
            clear()
            print(f"****** {BOLD}{C_UPDATETASK}ATUALIZAR STATUS{CRESET} ******")
            print("*" * 30 + "\n")
            try:
                task_id = int(input(f"{BOLD}ID da tarefa: {CRESET}"))
                status = input(f"{BOLD}Novo status: {CRESET}").lower()

                update_task(task_id, status)

            except ValueError:
                print(f"{BOLD}{RED}ID inválido. Precisa ser um número!{CRESET}")
                back()

        elif option == "4":
            clear()
            print(f"******* {BOLD}{C_DELETETASK}EXCLUIR TAREFA{CRESET} *******")
            print("*" * 30 + "\n")
            try:
                task_id = int(input(f"{BOLD}ID da tarefa: {CRESET}"))
                delete_task(task_id)
            except ValueError:
                print(f"{BOLD}{RED}ID inválido. Precisa ser um número!{CRESET}")
                back()

        elif option == "0":
            print(f"{BOLD}{RED}Saindo...{CRESET}")
            break

        else:
            print(f"{BOLD}{RED}*Opção inválida.{CRESET}")


#Chamada da função principal
main()