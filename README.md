### APIrest simples feita a partir de um CRUD CLI voltado à criação e gerenciamento de tarefas.

## 👷‍♀️ Funcionalidades
- Cadastro de usuário
e logando no seu usuário, você poderá realizar:

- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Remover tarefas
- Filtrar tarefas por texto
- Filtrar tarefas por status

## 🌌 Tecnologia usada 
- Python 3
- FastAPI
- Pydantic
- MongoDB
- PyMongo
- Docker
- Docker Compose

## 💻 Setup 

### 1. Abra o terminal e vá até um diretório vazio de sua escolha

### 2. Digite o comando para clonar o repositório:  
```bash
git clone -b feature/rest-api --single-branch https://github.com/abacax6/taskmanager.git
```

### 3. Entre na pasta "taskmanager" pelo terminal
```bash
cd taskmanager
```

### 4. Crie o arquivo .env
**Windows**
```bash
copy .env.example .env
```

**Linux/macOS**
```bash
cp .env.example .env
```

### 5. Suba toda a aplicação
```bash
docker compose up --build
```
**Esse comando deverá:**

- Construir a imagem da API
- Iniciar o container do MongoDB
- Iniciar o container da API FastAPI
- Configurar a comunicação entre os serviços

### 🚀 Utilização
**Após a inicialização dos containers, acesse:**
```bash
http://localhost:8000/docs
```
**O Swagger UI será exibido e permitirá testar todos os endpoints da aplicação diretamente pelo navegador.**

<img width="1463" height="904" alt="image" src="https://github.com/user-attachments/assets/1a411623-f99b-4851-8c35-53440454f166" />


### 🗄️ Banco de Dados
**A aplicação utiliza MongoDB para persistência dos dados.**

**Os dados permanecem armazenados em um volume Docker, permitindo que as tarefas continuem disponíveis mesmo após reinicializações dos containers.**

### 🛑 Encerrando a aplicação
**Para parar os containers:**
```bash
docker compose down
```

**Se desejar remover também os volumes de dados:**
```bash
docker compose down -v
```
