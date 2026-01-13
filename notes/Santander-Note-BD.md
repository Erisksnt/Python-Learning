# 🗃️ Banco de Dados - Conceitos Fundamentais

## 📌 O que é um Banco de Dados?
- Um **banco de dados** é uma coleção organizada de dados que pode ser acessada, gerenciada e atualizada de forma eficiente.
- É utilizado para **armazenar informações de forma estruturada**, garantindo persistência e integridade.
- Pode ser acessado por sistemas, aplicações ou usuários através de linguagens de consulta como **SQL**.

---

## 🧮 Banco de Dados Relacional (RDBMS)

### ✅ Características:
- Organiza os dados em **tabelas** com **linhas e colunas**.
- Cada tabela possui um **esquema fixo** (estrutura definida).
- Usa **chaves primárias e estrangeiras** para relacionar dados entre tabelas.
- Baseado em **lógica relacional** e consulta via **SQL (Structured Query Language)**.

### 📚 Exemplos:
- MySQL
- PostgreSQL
- Oracle
- Microsoft SQL Server

### ✔️ Vantagens:
- Consistência e integridade dos dados
- Ideal para sistemas com dados estruturados
- Suporte a transações (ACID)

---

## ⚖️ Formas Normais (Normalização)

### 📌 O que é?
- **Normalização** é o processo de organizar os dados em um banco de dados para evitar **redundâncias** e garantir **consistência**.
- Divide grandes tabelas em tabelas menores, com **relacionamentos bem definidos**.

### 🔢 Principais Formas Normais:

#### 1️⃣ Primeira Forma Normal (1FN)
- Elimina **grupos repetitivos**
- Cada campo deve conter **um único valor atômico**

#### 2️⃣ Segunda Forma Normal (2FN)
- Estar em 1FN **e** todos os atributos **dependem totalmente da chave primária**

#### 3️⃣ Terceira Forma Normal (3FN)
- Estar em 2FN **e** não possuir **dependências transitivas**
- Ou seja, nenhum campo deve depender de outro campo que não seja chave primária

---

## 🔧 SQL - Comandos Básicos

### 📌 Criar um banco de dados:
```sql
CREATE DATABASE nome_do_banco;
```

### 📌 Selecionar banco de dados:
```sql
USE nome_do_banco;
```

### 📌 Criar tabela:
```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100)
);
```

### 📌 Inserir dados:
```sql
INSERT INTO usuarios (nome, email)
VALUES ('Maria', 'maria@email.com');
```

### 📌 Consultar dados:
```sql
SELECT * FROM usuarios;
```

---

## 🗂️ Banco de Dados Não Relacional (NoSQL)

### ✅ Características:
- Flexível: **sem esquema fixo**
- Usado para dados sem estrutura definida ou que muda frequentemente
- Quatro principais tipos:
  - 🔸 **Documentos** (ex: MongoDB)
  - 🔹 **Chave-valor** (ex: Redis)
  - 🔸 **Colunar** (ex: Cassandra)
  - 🔹 **Grafos** (ex: Neo4j)

### 📚 Exemplos:
- MongoDB
- Redis
- Cassandra
- DynamoDB

### ✔️ Vantagens:
- Alta escalabilidade horizontal
- Performance com grandes volumes de dados
- Ótimo para aplicações em tempo real e Big Data

---

## 🔧 MongoDB com Python (usando pymongo)

### 📌 Instalação do driver:
```bash
pip install pymongo
```

### 📌 Conectar ao banco:
```python
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["nomeDoBanco"]
```

### 📌 Inserir documento:
```python
db.usuarios.insert_one({"nome": "Maria", "email": "maria@email.com"})
```

### 📌 Consultar documentos:
```python
for usuario in db.usuarios.find():
    print(usuario)
```

### 📌 Atualizar documento:
```python
db.usuarios.update_one(
    {"nome": "Maria"},
    {"$set": {"email": "novo@email.com"}}
)
```

### 📌 Remover documento:
```python
db.usuarios.delete_one({"nome": "Maria"})
```

---

## 🔍 Comparativo: Relacional vs Não Relacional

| Critério                | Relacional (SQL)              | Não Relacional (NoSQL)          |
|-------------------------|-------------------------------|----------------------------------|
| Estrutura               | Tabelas e colunas             | Documentos, grafos, chave-valor |
| Esquema                 | Rígido (pré-definido)         | Flexível                        |
| Linguagem               | SQL                           | Varia (JSON, consultas nativas) |
| Transações              | Suporte completo (ACID)       | Suporte limitado ou eventual    |
| Escalabilidade          | Vertical (mais poder à máquina)| Horizontal (mais máquinas)      |
| Ideal para              | Dados estruturados            | Dados semi ou não estruturados  |

---

## 💡 Quando Usar Qual?

- **Banco Relacional:**
  - Aplicações com dados estruturados e necessidade de integridade
  - ERP, sistemas bancários, gestão de estoque

- **Banco Não Relacional:**
  - Aplicações com dados variados e alta escalabilidade
  - Redes sociais, apps de mensagens, análise de logs, IoT
