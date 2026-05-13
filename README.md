# APIrest: Task Manager
### APIrest simples feita a partir de um CRUD CLI voltado à criação e gerenciamento de tarefas.

## Funcionalidades (Você já conhece!)
- Criar tarefas
- Listar tarefas
- Atualizar status
- Remover tarefas

## Tecnologia usada
- Python 3
- FastAPI
- Pydantic

## Como baixar/obter
1. Assegure-se de ter o python instalado e a biblioteca fastAPI:
```bash
pip install "fastapi[standard]"
```

2. Abra o terminal e vá até um diretório vazio
   
3. Digite o comando para clonar o repositório:  
```bash
git clone -b feature/rest-api --single-branch https://github.com/abacax6/taskmanager.git
```

## Como executar
1. Abrindo o seu terminal na pasta "taskmanager", dentro do diretório onde você clonou o repositório, digite:
```bash
python -m uvicorn api:app --reload 
```
O servidor deverá começar a rodar.

2. Você agora pode testar o APIrest no seu http://localhost:8000/docs#/ através do navegador! 😁
<img width="1498" height="552" alt="image" src="https://github.com/user-attachments/assets/8030502a-4e45-4967-b6a0-a42b1ee6620f" />

