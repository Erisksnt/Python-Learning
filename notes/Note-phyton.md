
# 📘 Anotações de Python

## 🛠️ Comandos Básicos

- `dir` — Verifica a estrutura e os atributos disponíveis de um objeto.
- `help()` — Ajuda interativa dentro do próprio Python.
- `input()` — Solicita uma entrada do usuário.
- `print()` — Exibe valores na tela.

## 📌 Tipos de Dados

- `int` — Número inteiro.
- `float` — Número com casas decimais.
- `bool` — Booleano (True ou False, 1 ou 0).
- `str` — Texto (string/caractere).

## 🧠 Operadores Lógicos

- `and` — E lógico.
- `or` — Ou lógico.
- `not` — Negação lógica.
- `in`, `is`, `is not` — Operadores de comparação e identidade.

## 🔁 Estruturas de Repetição

- `while` — Executa enquanto a condição for verdadeira.
- `for` — Loop com controle de condição ou intervalo.

## ✅ Estruturas Condicionais

- `if` — Se a condição for verdadeira, executa o bloco.
- `elif` — Caso contrário, se essa outra condição for verdadeira.
- `else` — Executado se nenhuma condição for satisfeita.

## 🧩 Funções

- `def` — Define uma função.
  
```python
def minha_funcao():
    print("Olá!")
```

## 📚 Listas

- `list` — Estrutura para armazenar múltiplos valores mutáveis.

```python
minha_lista = [1, 2, 3]
```

### Métodos de Lista

- `.append(x)` — Adiciona um item ao final.
- `.clear()` — Limpa todos os itens da lista.
- `.copy()` — Cria uma cópia da lista.
- `.count(x)` — Conta quantas vezes um item aparece.
- `.extend(lista2)` — Junta duas listas.
- `.index(x)` — Retorna o índice do item.
- `.pop()` — Remove e retorna o último item.
- `.remove(x)` — Remove um item específico.
- `.reverse()` — Inverte a ordem dos elementos.
- `.sort()` — Ordena em ordem crescente.
- `.sort(key=lambda x: len(x))` — Ordena com base no comprimento dos itens.
- `len(lista)` — Retorna o número de elementos.

## 📐 Tuplas

- `tuple` — Estrutura imutável.

```python
tupla = ("a", "b", "c")
```

## 🎯 Sets (Conjuntos)

- `set` — Estrutura de dados sem elementos duplicados.

```python
meu_set = {"a", "b", "c"}
```

## ⏳ Datas e Horas

> É necessário importar a biblioteca:

```python
from datetime import date, datetime, time, timedelta
```

- `date` — Representa uma data.
- `time` — Representa um horário.
- `datetime` — Representa data e hora.
- `datetime.today()` — Retorna a data e hora atual.
- `datetime.timedelta()` — Faz operações com datas.
- `strftime()` — Converte objeto `datetime` em string com formato.
- `strptime()` — Converte string formatada em objeto `datetime`.

# 📘 Programacao Orientada a Objetos (POO)

A Programacao Orientada a Objetos é um paradigma de programação que se baseia no uso de **classes** e **objetos**. Com ela, conseguimos organizar o código de forma mais modular e reutilizável.

---

## 🔹 Conceitos Iniciais

### ✅ Atributos

Atributos são **características** ou **propriedades** de uma classe. Exemplo:

```python
class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
```

---

## 💠 Método Construtor (`__init__`)

O método construtor é usado para **inicializar os atributos** do objeto assim que ele é criado.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

---

## 🧹 Método Destrutor (`__del__`)

Executado automaticamente quando o objeto é destruído. Pode ser usado para liberar recursos.

```python
class Pessoa:
    def __del__(self):
        print("Objeto destruído")
```

---

## 🧬 Herança

Permite que uma classe **filha** herde atributos e métodos de uma **classe pai**.

```python
class Animal:
    def falar(self):
        print("Som genérico")

class Cachorro(Animal):
    pass

dog = Cachorro()
dog.falar()  # Saída: Som genérico
```

---

## ✅ Benefícios da Herança

- Representa relações do **mundo real**;
- **Reutilização de código** (evita duplicacoes);
- Permite **extensão de funcionalidades** sem modificar a classe original;
- **Transitividade**: se B herda de A, e C herda de B, então C também herda de A.

```python
class A: pass
class B(A): pass
class C(B): pass
```

---

## 🔀 Herança Múltipla

Quando uma classe **herda de duas ou mais** classes ao mesmo tempo.

```python
class Mamifero:
    def andar(self):
        print("Andando")

class Aquatico:
    def nadar(self):
        print("Nadando")

class Onitorrinco(Mamifero, Aquatico):
    pass

bicho = Onitorrinco()
bicho.andar()
bicho.nadar()
```

---

## 🔑 `**kwargs`

`**kwargs` permite passar um número variável de argumentos nomeados (chave=valor) para uma função.

```python
def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Erick", idade=23)
```

---

## 📚 `__mro__` (Method Resolution Order)

Mostra a ordem de busca dos métodos na hierarquia de herança. Útil para entender como Python resolve métodos em herança múltipla.

```python
class A: pass
class B(A): pass
class C(B): pass

print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

---

📌 **Resumo:**\
POO é fundamental para a construção de sistemas organizados e reutilizáveis. Os conceitos de atributos, métodos, herança, e funcionalidades como `**kwargs` e `__mro__` tornam o código mais flexível e poderoso.

# 🔐 Encapsulamento, Propriedades e Polimorfismo em POO

## 🔹 O que é Encapsulamento?

Encapsulamento é um dos pilares da Programação Orientada a Objetos. Ele permite **esconder os detalhes internos de uma classe** e **restringir o acesso direto aos atributos**.

> ✅ Objetivo: proteger o estado interno do objeto e fornecer métodos controlados para interação.

### ✅ Atributos Públicos, Protegidos e Privados

| Tipo        | Convenção        | Descrição |
|-------------|------------------|-----------|
| Público     | `self.nome`      | Pode ser acessado de fora da classe |
| Protegido   | `self._nome`     | Deve ser acessado apenas dentro da classe ou subclasses |
| Privado     | `self.__nome`    | Não deve ser acessado diretamente fora da classe |

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome         # público
        self._cpf = "123456789"  # protegido
        self.__senha = "abc123"  # privado
```


# 🧩 Propriedades em Python

Em Python, usamos **propriedades** para controlar o acesso aos atributos de uma classe, aplicando o conceito de **encapsulamento**. Isso permite que métodos sejam acessados como se fossem atributos.

---

## 🔸 @property

Permite transformar um método em um atributo de **somente leitura**. Muito útil para cálculos derivados de atributos privados.

### Exemplo:

```python
class Pessoa:
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        ano_atual = 2025
        return ano_atual - self._ano_nasc
```

---

## 🔸 @x.setter

Permite definir um **método de escrita** para um atributo decorado com `@property`. Assim, podemos atribuir valores usando `obj.atributo = valor`.

### Exemplo:

```python
class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor
```

---

## 🔸 @x.deleter

Permite deletar um atributo controlado, usando `del obj.atributo`. Útil quando queremos controlar ou evitar que dados sejam removidos sem validação.

### Exemplo:

```python
class Produto:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.deleter
    def nome(self):
        print("Deletando nome...")
        del self._nome
```

---

## 🎭 Polimorfismo

Polimorfismo é a capacidade de **usar métodos com o mesmo nome em classes diferentes**, com comportamentos distintos.  
Isso permite escrever **código genérico**, facilitando a extensibilidade e reutilização.

### 📌 Exemplo:

```python
class Animal:
    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Latido")

class Gato(Animal):
    def emitir_som(self):
        print("Miado")

# Uso polimórfico:
animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    animal.emitir_som()
```

📝 Mesmo chamando `emitir_som()`, o comportamento muda conforme a classe do objeto.

---

## 👨‍👩‍👧‍👦 Polimorfismo com Herança

O polimorfismo é frequentemente usado com **herança**.  
Uma **superclasse** define métodos genéricos, e as **subclasses** os implementam de formas diferentes.

Isso permite que você trate diferentes objetos de forma uniforme usando a classe base, mas com comportamentos distintos.

---

## 🧮 Variáveis de Classe vs Variáveis de Instância

- **Variáveis de instância** são únicas para cada objeto (definidas dentro do `__init__` com `self`).
- **Variáveis de classe** são compartilhadas entre todas as instâncias (definidas diretamente na classe).

### 📌 Exemplo:

```python
class Pessoa:
    especie = "Humano"  # variável de classe

    def __init__(self, nome):
        self.nome = nome  # variável de instância
```

---

## 🔧 Métodos de Classe vs Métodos Estáticos

- **@classmethod**  
  Recebe a classe como primeiro argumento (`cls`) e pode modificar atributos da classe.

- **@staticmethod**  
  Não recebe automaticamente `self` ou `cls`. Funciona como uma função comum dentro da classe.

### 🧭 Quando usar?

- Use `@classmethod` quando o método precisar acessar ou modificar a **classe**.
- Use `@staticmethod` para funções **utilitárias** relacionadas à classe, mas que não precisam da instância nem da classe.

---

## 🧱 Classes Abstratas

Classes abstratas definem uma **estrutura base** para outras classes. Elas **não devem ser instanciadas diretamente**.

Utilizam:

- O módulo `abc`
- O decorador `@abstractmethod`

Esses elementos forçam que subclasses implementem determinados métodos.

> ⚠️ Uma vez que uma classe se torna abstrata, **ela não pode mais ser instanciada diretamente**.

---

## 🧩 Interfaces

Interfaces determinam **o que uma classe deve fazer, mas não como**.  
São como contratos: qualquer classe que a implemente **precisa fornecer os métodos definidos** com sua própria lógica.

Em Python, interfaces geralmente são representadas com:

- `ABC` (Abstract Base Class)
- Métodos decorados com `@abstractmethod`

---

## 🧪 Modo ABC (Abstract Base Class)

O módulo `abc` permite criar **classes abstratas** no Python.

### 🔧 Como usar:

1. Importe `ABC` e `abstractmethod` do módulo `abc`.
2. Crie uma classe base que herda de `ABC`.
3. Use `@abstractmethod` para definir os métodos obrigatórios.

### 📌 Exemplo:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass
```
# 📦 Resumo sobre Packages e Publicação no PyPI

## 📁 O que são Packages?

Packages em Python são conjuntos de módulos organizados para facilitar a **reutilização de código**. Eles ajudam a manter o projeto modular, colaborativo e fácil de instalar ou distribuir.

## 🧪 Por que testar no TestPyPI antes?

Antes de publicar um pacote no repositório oficial do PyPI, é **essencial testar** no ambiente de testes:

🔗 [TestPyPI](https://test.pypi.org/project)

### ✅ Vantagens de testar:
- Verificar se o pacote instala corretamente.
- Validar os metadados como `setup.py`.
- Corrigir possíveis erros sem afetar o repositório oficial.

🧑‍💻 Após os testes, o pacote pode ser publicado no:

🔗 [PyPI Oficial](https://pypi.org/project)

---

# 🤖 Resumo sobre IA Generativa e Conceitos Relacionados

## ✨ O que é IA Generativa?

É uma área da inteligência artificial que cria **conteúdos originais** como texto, imagens, áudio ou código com base em dados aprendidos. Exemplos: **ChatGPT, DALL·E**.

---

## 📚 Modelos de Linguagem Grandes (LLMs)

- **Tokenização**: Quebra de texto em pequenas unidades (tokens) para análise.
- **Embeddings**: Transformação de palavras em vetores numéricos.
- **Atenção (Attention)**: Técnica que foca nas partes mais importantes do input (usada em Transformers).

---

## 💬 Engenharia de Prompts

Técnica que melhora os resultados fornecidos por IA generativa ao **formular perguntas ou comandos mais estratégicos**.

📌 Exemplo: usar frases como *"Explique passo a passo..."* para obter respostas mais completas.

---

## 📈 Modelo de Regressão

Modelo usado para prever **valores contínuos** (ex: temperatura, preço de uma casa) com base em dados de entrada.

---

## 🧠 Tipos de Aprendizado de Máquina

- **Supervisionado**: Usa dados com rótulos (ex: classificar e-mails como spam ou não).
- **Não supervisionado**: Descobre padrões em dados sem rótulos (ex: agrupamentos).
- **Por reforço**: Aprende com recompensas ou punições (ex: jogos e robôs).

---

## 🧬 Redes Neurais & Deep Learning

- **Rede Neural**: Conjunto de nós (neurônios artificiais) que simulam o funcionamento do cérebro.
- **Deep Learning**: Versão avançada com **múltiplas camadas**, ideal para reconhecer padrões complexos.

---

## ☁️ Azure Machine Learning

Plataforma da Microsoft que permite criar, treinar e implantar modelos de ML de forma **escalável e integrada à nuvem**.

---

## 🗣️ Processamento de Linguagem Natural (NLP)

Área da IA que permite a **compreensão da linguagem humana** por computadores.

🌟 Aplicações:
- Tradução automática  
- Análise de sentimentos  
- Chatbots inteligentes  
