#Usando propiedades usando o Exemplo Foo
class Foo:
    def __init__(self, x=None):
        self._x = x
    
    #Para retornar valor precisa obrigatoriamente ter o property
    @property
    def x(self):
        return self._x or 0
    
    #Para alterar o valor precisa do x.setter
    @x.setter
    def x(self, value):
        self._x += value
    
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)