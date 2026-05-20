# 📊 APIrest: Task Manager 
### APIrest simples feita a partir de um CRUD CLI voltado à criação e gerenciamento de tarefas.

## 👷‍♀️ Funcionalidades (Você já conhece!) 
- Criar tarefas
- Listar tarefas
- Atualizar status
- Remover tarefas

## 🌌 Tecnologia usada 
- Python 3
- FastAPI
- Pydantic

## 💻 Setup 

### 1. Abra o terminal e vá até um diretório vazio de sua escolha

### 2. Digite o comando para clonar o repositório:  
```bash
git clone -b feature/rest-api --single-branch https://github.com/abacax6/taskmanager.git
```

### 3. Entre na pasta "taskmanager" pelo terminal

### 4. Criar ambiente virtual
```bash
python -m venv venv
```

### 5. Ativar ambiente virtual
**Windows**
```bash
venv\Scripts\activate
```

**Linux/macOS**
```bash
source venv/bin/activate
```

### 6. **Instalar dependências**
```bash
pip install -r requirements.txt
```

### 7. **Rodar API**
```bash
python -m uvicorn api:app --reload
```
O servidor deverá começar a rodar.

### 8. Você agora pode testar o APIrest no seu http://localhost:8000/docs#/ através do navegador! 😁
<img width="1498" height="552" alt="image" src="https://github.com/user-attachments/assets/8030502a-4e45-4967-b6a0-a42b1ee6620f" />

