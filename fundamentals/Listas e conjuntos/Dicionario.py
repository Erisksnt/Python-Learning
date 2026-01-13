#Dicionario em python

#para informar um dicionario usasse {} e ao lado do item que quer acrescentar, usa-se ":"
pessoa = {"nome": "Erick", "idade": 28}

#Outra fora é utilizando o "dict"
pessoa = dict(nome="Erick", idade=28)

#Outra forma de quando ja tem um dicionario criado e eu quero acrescentar uma nova chave.
pessoa["telefone"] = "4002-8922"
print(pessoa)

#////////////////////////////////////////////////////////
#Dicionario aninhado (quando eu tenho um dicionario de conjunto e desejo puxar um valor especifico relacionado ao item)
contatos = {

"erick@gmail.com": {"nome": "Erick", "telefone": "3333-2221"},
"brunno@gmail.com": {"nome": "Brunno", "telefone": "3443-2121"},
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3344-9871"},
"rian@gmail.com": {"nome": "Rian", "telefone": "3333-7766"},
}
telefone = contatos["guilherme@gmail.com"]["telefone"] # "3344-9871"​
print(telefone)

#///////////////////////////////////
#Iterando o dicionario  
 
for chave in contatos:
    print(chave, contatos[chave])

# .items retorna uma lista de tuplas
for chave, valor in contatos.items():
    print(chave, valor)


# .dromkeys cria uma chave dentro do dicionario
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}​
dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}​

# .get acessa valor dentro do dicionario (ele informa se essa chave existe no dicionario também)
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
contatos.get("chave", {}) # ele retorna "{}" pq ele não encontrou o argumento​
contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}​

# .keys retorna apenas as chaves do dicionario
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.keys() # dict_keys(['guilherme@gmail.com'])​

# .popitem remove os itens 1 a 1
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.popitem()

# .setdefault

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}
}
contatos.setdefault("nome", "Felipe")
print(contatos)

# .values retorna todos os valores ligados a 1 chave
 
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.values()
