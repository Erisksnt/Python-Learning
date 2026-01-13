# 🐍 Anotações de Python - Conceitos Avançados

## Funções como objetos de primeira classe
- Em Python, funções são objetos de primeira classe.
- Isso significa que podem ser:
  - Atribuídas a variáveis
  - Passadas como argumentos
  - Retornadas por outras funções
- Exemplo:
  ```python
  def do_something(name):
      print(f"Olá, {name}")

  def executar(funcao):
      funcao("Erick")

  executar(do_something)
  ```

## Funções internas (Inner Functions)
- É possível definir funções dentro de outras funções.
- Isso permite encapsular lógicas que só fazem sentido localmente.
- Exemplo:
  ```python
  def pai():
      print("oi")

      def filho():
          return "tchau"

      return filho()

  resultado = pai()
  print(resultado)  # tchau
  ```

## Decoradores
- Decoradores adicionam comportamentos antes/depois de uma função ser executada.
- São úteis para validações, autenticações, logs etc.
- Exemplo:
  ```python
  def meu_decorador(func):
      def wrapper():
          print("Antes da função")
          func()
          print("Depois da função")
      return wrapper

  @meu_decorador
  def saudacao():
      print("Olá mundo")

  saudacao()
  ```

## Introspecção
- É a capacidade de examinar objetos em tempo de execução (runtime).
- Usada para debugging, metaprogramação e validações dinâmicas.
- Funções úteis:
  ```python
  type(obj)
  dir(obj)
  hasattr(obj, "atributo")
  getattr(obj, "atributo", valor_padrao)
  ```

## Iteradores
- São objetos que implementam os métodos `__iter__()` e `__next__()`.
- Permitem percorrer itens um a um.
- Usados em loops `for`, `in`, etc.
- Exemplo:
  ```python
  class Contador:
      def __init__(self, limite):
          self.limite = limite

      def __iter__(self):
          self.atual = 0
          return self

      def __next__(self):
          if self.atual < self.limite:
              self.atual += 1
              return self.atual
          raise StopIteration
  ```

## Geradores
- Geradores são um tipo especial de iterador criado com funções que usam `yield`.
- Economizam memória: produzem valores sob demanda.
- Exemplo:
  ```python
  def contador_pares(maximo):
      n = 0
      while n <= maximo:
          yield n
          n += 2
  ```

### Características dos Geradores
- Estado interno mantido entre chamadas.
- Interrompe em `yield` e continua da próxima vez.
- Depois de iterado, não pode ser reiniciado.

### Quando usar:

| Situação                | Usar           | Vantagem                   |
|-------------------------|----------------|----------------------------|
| Fluxo simples           | Geradores      | Menor uso de memória       |
| Lógica mais complexa    | Iteradores     | Maior controle do processo |


## 🧾 Manipulação de Arquivos
### Por que manipular arquivos?
- Para salvar dados de forma persistente (além da execução do programa).

## Erros comuns:
- `FileNotFoundError`: arquivo não encontrado.
- `PermissionError`: falta de permissão de acesso.
- `IOError`: erro de entrada/saída (como disco cheio).
- `UnicodeDecodeError`: erro ao tentar ler arquivo com codificação incorreta.
- `UnicodeEncodeError`: erro ao tentar escrever conteúdo mal codificado.

## 📦 Pacotes em Python

### O que são pacotes?
- Conjuntos de módulos organizados em diretórios com um arquivo `__init__.py`.
- Permitem reutilizar e compartilhar código.

## Pip - Gerenciador de Pacotes
- Instala, atualiza e remove pacotes Python.
- Comandos principais:
  ```bash
  pip install nome_do_pacote
  pip uninstall nome_do_pacote
  pip list
  pip install --upgrade nome_do_pacote
  ```

## Criando ambiente virtual
- Para isolar dependências por projeto:
  ```bash
  python3 -m venv myenv
  source myenv/bin/activate  # Linux/Mac
  myenv\Scripts\activate     # Windows
  ```

