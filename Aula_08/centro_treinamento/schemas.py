from pydantic import Field
from typing_extensions import Annotated
from Aula_08.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome:Annotated[str, Field(description = 'Nome do centro de treinamento', exemple='Treiner Center', max_length=20)]
    endereco:Annotated[str, Field(description = 'Endereço de treinamento', exemple='casa dos bobo,n° 0', max_length=60)]
    prorpietario:Annotated[str, Field(description = 'Proprietario de treinamento', exemple='Erick', max_length=30)]