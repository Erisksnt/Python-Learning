from pydantic import Field
from typing_extensions import Annotated
from Aula_08.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome:Annotated[str, Field(description = 'Nome da Categoria', exemple='scale', max_length=50)]