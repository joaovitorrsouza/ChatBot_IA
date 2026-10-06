# Chatbot IA — FastAPI + Docker + OpenAI API

API de chatbot desenvolvida em **Python** com **FastAPI**, integrando a API da OpenAI para geração de respostas a mensagens enviadas por requisições HTTP.

O foco do projeto é demonstrar como encapsular uma integração com um serviço externo de IA dentro de uma aplicação Back-End simples, modular e executável em container.

## Stack

- Python 3.10+
- FastAPI
- Pydantic
- OpenAI Python SDK
- Uvicorn
- Docker

## Funcionalidades

- endpoint HTTP para envio de prompts
- integração com a API da OpenAI
- validação da entrada com Pydantic
- separação entre camada HTTP e lógica de integração
- execução com Uvicorn
- containerização com Docker

## Estrutura

```text
chatbot_ia/
├── app/
│   └── chatbot.py
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

## Endpoint

### `POST /chat`

Requisição:

```json
{
  "prompt": "Olá, tudo bem?"
}
```

Resposta:

```json
{
  "response": "Resposta gerada pelo modelo configurado na aplicação."
}
```

## Configuração

A integração utiliza a variável de ambiente:

```text
OPENAI_API_KEY
```

Crie um arquivo `.env`:

```env
OPENAI_API_KEY=sua-chave-aqui
```

> Nunca publique sua chave de API no repositório.

## Execução com Docker

### Build

```bash
docker build -t chatbot-ia ./chatbot_ia
```

### Execução

```bash
docker run -p 8000:8000 --env-file .env chatbot-ia
```

A API ficará disponível em:

```text
http://localhost:8000
```

## Teste com curl

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Olá, tudo bem?"}'
```

## O que este projeto demonstra

- desenvolvimento de API com FastAPI
- integração entre serviços
- consumo de API externa
- validação de dados
- organização modular
- uso de variáveis de ambiente
- containerização com Docker

## Próximas evoluções

- autenticação
- rate limiting
- logs estruturados
- persistência de histórico
- testes automatizados
- configuração externa do modelo utilizado
