from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

from Aula_08.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do Atleta', exemple='Erick', max_length=50)]
    cpf:  Annotated[int, Field(description = 'CPF do Atleta', exemple='12345678900', max_length=11)]
    idade:  Annotated[int, Field(description = 'idade do Atleta', exemple='23')]
    peso:  Annotated[PositiveFloat, Field(description = 'Peso do Atleta', exemple='65.5', )]
    altura:  Annotated[PositiveFloat, Field(description = 'Altura do Atleta', exemple='1.78')]
    sexo:  Annotated[str, Field(description = 'Sexo do Atleta', exemple='M', max_length=1)]