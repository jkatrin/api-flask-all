# 🚀 Desafio: Deploy Completo de uma API com Persistência e CI/CD

Este desafio tem como objetivo construir uma API RESTful em Python que receba dados de usuários, salve em um banco de dados MySQL, e seja totalmente automatizada com Docker, Terraform e GitHub Actions.

---

## 🎯 Objetivo

- Criar uma API em Python que receba dados via JSON e salve no MySQL.
- Containerizar a aplicação com Docker.
- Publicar a imagem no DockerHub.
- Provisionar uma instância EC2 com Terraform na AWS.
- Automatizar o deploy usando GitHub Actions.

---

## 📥 Entrada da API

### Rota: `POST /usuarios`

```json
{
  "nome": "Ana",
  "idade": 25,
  "altura": 1.65,
  "genero": "feminino"
}
```

---

## 📤 Saída esperada

```json
{
  "message": "Usuário salvo com sucesso",
  "id": 1
}
```

---

## 🗃️ Banco de Dados

- Banco: **MySQL**
- Tabela: `usuarios`
- Colunas:
  - `id` (auto increment, chave primária)
  - `nome` (varchar)
  - `idade` (int)
  - `altura` (float)
  - `genero` (varchar)

---

## 📦 Stack Técnica

- **Python** (Flask ou FastAPI)
- **MySQL**
- **Docker** e **Docker Compose**
- **Terraform** (AWS EC2)
- **GitHub Actions** (CI/CD)
- **DockerHub** (publicação de imagem)

---

## 📁 Estrutura do Projeto (Sugerida)

```
api/
├── app.py
├── models.py
├── database.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
terraform/
├── main.tf
├── variables.tf
└── modules/
    └── ec2/
        └── main.tf
        └── variables.tf
        └── outputs.tf
.github/
└── workflows/
    └── deploy-app.yml
    └── deploy-infra.yml
README.md
```

---

## 🧪 Funcionalidades da API

- [x] `POST /usuarios`: Salva dados de usuário no banco.
- [x] `GET /usuarios`: Lista todos os usuários cadastrados.

---

## ⚙️ Etapas do Desafio

### 1. Desenvolver a API em Python
- Criar endpoints para salvar e listar usuários.
- Conectar com banco MySQL usando SQLAlchemy ou `mysql-connector-python`.

### 2. Containerizar com Docker
- Criar um `Dockerfile` que:
  - Instala as dependências.
  - Expõe a porta da API.
  - Executa a aplicação.

### 3. Criar docker-compose.yml
- Subir API e banco MySQL localmente para testes.
- Utilizar variáveis de ambiente com `.env`.

### 4. Subir imagem no DockerHub
- Criar conta e repositório.
- Autenticar e fazer `docker push`.

### 5. Provisionar Infraestrutura com Terraform
- Criar uma instância EC2 Ubuntu.
- Liberar portas 22 (SSH) e 80 (HTTP).
- Instalar Docker via provisionamento remoto (`remote-exec`).
- Rodar o container com a imagem do DockerHub.

### 6. Automatizar com GitHub Actions
- Criar pipeline com os jobs:
  - `build`: Build da imagem Docker.
  - `push`: Envia imagem ao DockerHub.
  - `deploy`: Acessa EC2 via SSH e faz o deploy da nova imagem.

---

## 🔐 GitHub Secrets Necessários

| Variável           | Descrição                            |
|--------------------|----------------------------------------|
| `DOCKER_USERNAME`  | Usuário do DockerHub                  |
| `DOCKER_PASSWORD`  | Senha/token do DockerHub              |
| `EC2_HOST`         | IP público da EC2                     |
| `EC2_USER`         | Usuário SSH (ex: `ubuntu`)            |
| `AWS_SSH_KEY`      | Chave privada (formato PEM, base64)   |

---

## ✅ Critérios de Entrega

- [ ] API funcional com rotas `/usuarios` (GET e POST).
- [ ] Conexão com banco MySQL via Docker Compose.
- [ ] Imagem Docker publicada no DockerHub.
- [ ] Infraestrutura provisionada com Terraform.
- [ ] CI/CD funcionando com GitHub Actions.

---

## 🧠 Extras (opcional)

- Armazenar variáveis sensíveis no AWS SSM Parameter Store.
- Usar NGINX como proxy reverso.

---# api-docker
