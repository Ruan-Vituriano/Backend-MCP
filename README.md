# 🌱 Backend-MCP — Assistente Inteligente para Agricultura

Backend de um sistema inteligente para gestão de plantio de hortaliças, com foco em uso de IA como assistente para agricultores.

O sistema permite que o usuário faça perguntas e receba respostas baseadas em conhecimento técnico (RAG) e, futuramente, ações reais (MCP).

---

# 🧠 Visão Geral

Este projeto implementa um backend utilizando IA para auxiliar agricultores com:

* Recomendações de plantio
* Informações sobre culturas
* Suporte baseado em contexto agrícola
* Expansão futura com integração a dados reais (clima, solo, etc.)

---

# ⚙️ Arquitetura

```
Frontend (Angular)
        ↓
Backend (FastAPI)
        ↓
Camada de IA
   ├── RAG (conhecimento)
   └── MCP (ações - futuro)
        ↓
Bancos de dados
```

---

# 🚀 Tecnologias Utilizadas

* Python
* FastAPI
* Uvicorn
* Gemini API (Google AI)
* Python-dotenv

---

# 📁 Estrutura do Projeto

```
backend-MCP/
 ├── app/
 │   ├── routes/        # Endpoints da API
 │   ├── services/      # Regras de negócio
 │   ├── ai/
 │   │   ├── rag/       # Recuperação de contexto (RAG)
 │   │   ├── mcp/       # Tools / ações (em desenvolvimento)
 │   │   ├── agent.py   # Orquestrador da IA
 │   ├── models/        # Modelos de dados
 │   ├── db/            # Conexão com banco
 │   └── core/          # Configurações globais
```

---

# 🔄 Fluxo de Funcionamento

1. Usuário envia uma pergunta
2. Backend recebe via endpoint `/chat`
3. O sistema:

   * Busca contexto relevante (RAG)
   * Monta um prompt
   * Envia para o modelo Gemini
4. A IA gera uma resposta contextualizada
5. Resposta é retornada ao usuário

---

# 🤖 Integração com IA

O projeto utiliza a API do Gemini para geração de respostas.

Modelo atual:

```
gemini-2.5-flash
```

---

# 📚 RAG (Retrieval-Augmented Generation)

Atualmente o sistema utiliza um RAG simples em memória com documentos estáticos.

### Objetivo futuro:

* Integração com banco vetorial (ChromaDB)
* Busca semântica mais precisa
* Base de conhecimento agrícola mais robusta

---

# 🛠️ MCP (Model Context Protocol)

Ainda em desenvolvimento.

Planejado para permitir que a IA:

* Consulte clima em tempo real
* Acesse dados do usuário
* Gere recomendações baseadas em contexto real

---

# ▶️ Como rodar o projeto

## Pré-requisitos

* Python 3.12+ instalado
* PowerShell no Windows
* Uma chave válida da Gemini API
* Preferencialmente usar um caminho de projeto sem acentos no Windows, caso encontre erro de encoding durante a instalação

## 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd backend-MCP
```

---

## 2. Crie e ative o ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, execute antes:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

---

## 3. Instale as dependências

```powershell
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## 4. Configure as variáveis de ambiente

Crie um arquivo `.env`:

```
GEMINI_API_KEY=sua_chave_aqui
```

> Sem essa variável o backend pode subir, mas a rota `/chat` não conseguirá gerar respostas.

---

## 5. Execute o servidor

```powershell
uvicorn app.main:app --reload
```

---

## 6. Acesse a documentação

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Exemplo de requisição

### POST `/chat`

```json
{
  "pergunta": "Qual o melhor clima para plantar alface?",
  "user_id": 1
}
```

---

# 🔥 Roadmap

## ✅ Atual

* [x] Estrutura do backend
* [x] Integração com IA (Gemini)
* [x] RAG básico em memória
* [x] Endpoint de chat funcional

---

## 🚧 Em desenvolvimento

* [ ] RAG com banco vetorial (ChromaDB)
* [ ] Implementação de MCP (tools)
* [ ] Persistência com PostgreSQL
* [ ] Personalização por usuário

---

## 🚀 Futuro

* [ ] Integração com API de clima
* [ ] Recomendações inteligentes por região
* [ ] Diagnóstico de pragas
* [ ] IA proativa (alertas automáticos)

---

# ⚠️ Observações

* O projeto está em fase inicial (MVP)
* A qualidade das respostas depende da base de conhecimento (RAG)
* A arquitetura foi pensada para escalar com novas features de IA
* Se aparecer erro de instalação em `psycopg2-binary` no Windows, tente clonar o projeto em um caminho sem acentos e recriar o ambiente virtual


---

# 💡 Objetivo do Projeto

Criar um assistente inteligente que realmente ajude agricultores na tomada de decisão, utilizando IA de forma prática e acessível.
