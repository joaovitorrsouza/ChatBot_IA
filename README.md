# 🤖 Chatbot com Python, FastAPI, Docker e OpenAI

Este projeto é uma API de chatbot desenvolvida em **Python** com **FastAPI**, utilizando a API da **OpenAI (GPT-3.5-turbo)** para gerar respostas inteligentes a mensagens recebidas. Toda a aplicação é containerizada com **Docker**, facilitando o deploy em qualquer ambiente.

---

## 📌 Funcionalidades

- Envio de mensagens via requisição HTTP `POST`  
- Respostas geradas dinamicamente por inteligência artificial  
- Código limpo e modular  
- Docker para execução em ambientes isolados  
- Pronto para deploy em nuvem ou local  

---

## 🧰 Tecnologias utilizadas

- Python 3.10+  
- FastAPI  
- OpenAI Python SDK (>= 1.0)  
- Uvicorn (servidor ASGI)  
- Docker  

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-ia.git
cd chatbot-ia
```

### 2. Configure a chave da API da OpenAI

Crie uma conta em:  
https://platform.openai.com/account/api-keys

Depois, crie um arquivo `.env` no diretório raiz com o seguinte conteúdo:

```
OPENAI_API_KEY=sua-chave-aqui
```

Substitua `sua-chave-aqui` pela sua chave real.

---

### 3. Construa a imagem Docker

Com o Docker instalado e rodando, execute:

```bash
docker build -t chatbot-ia .
```

---

### 4. Execute o container

```bash
docker run -p 8000:8000 --env-file .env chatbot-ia
```

A API estará disponível em:  
http://localhost:8000

---

## 📡 Como testar a API

### Endpoint: `POST /chat`

**Requisição:**

```json
{
  "prompt": "Olá, tudo bem?"
}
```

**Resposta esperada:**

```json
{
  "response": "Olá! Estou aqui para te ajudar. Em que posso ser útil hoje?"
}
```

---

## 🔬 Exemplos de testes

### Usando `curl`:

```bash
curl -X POST http://localhost:8000/chat   -H "Content-Type: application/json"   -d "{"prompt":"Olá, tudo bem?"}"
```

### Usando Postman ou Insomnia:

- Método: `POST`  
- URL: `http://localhost:8000/chat`  
- Body (raw JSON):

```json
{
  "prompt": "Olá, tudo bem?"
}
```


---

## 📄 Dockerfile utilizado

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🧠 Sobre a API da OpenAI

Este projeto utiliza o modelo **gpt-3.5-turbo** da OpenAI para gerar respostas inteligentes e contextuais.  
Documentação oficial: https://platform.openai.com/docs


## ✅ Melhorias futuras

- [ ] Interface Web (ex: Streamlit ou React)  
- [ ] Autenticação com JWT  
- [ ] Registro de logs de conversas  
- [ ] Limite de uso por IP ou chave  

---
