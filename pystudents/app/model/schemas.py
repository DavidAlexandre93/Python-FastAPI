"""
Leiaute dos dados utilizados pelo pydantic para validação dos mesmos.
"""
import re
from typing import Any

from pydantic import BaseModel, validator

from app.enumerators.enumerators import StatesBrEnum as StatesEnum

POSTAL_CODE_REGEX = re.compile("[0-9]{5}\\-[0-9]{3}")

"""
Define a estrura de dados que armazena as informações dos estudantes.
"""


class StudentBaseSchema(BaseModel):
    name: str
    address: str
    neighbour: str
    city: str
    postal_code: str


"""
Verifica se o CEP tem cinco números, hífen e três números.
"""


@validator("postal_code", allow_reuse=True)
async def validate_postal_code(cls, v: str, **kwargs: int) -> str:
    if not POSTAL_CODE_REGEX.match(postal_code := v.rjust(9, "0")):
        raise ValueError("O CEP informado é inválido!")

    return postal_code


"""
Esquema de dados para ser usado na criação de novos estudantes.
"""


class CreateStudentSchema(StudentBaseSchema):
    state: StatesEnum


"""
Esquema de dados para ser usado para visualização dos estudantes.
"""


class StudentSchema(StudentBaseSchema):
    id: int
    state: StatesEnum


"""
Esquema de dados para a atualização dos dados dos estudantes.
"""


class UpdateStudentSchema(StudentBaseSchema):
    name: str = ""
    address: str = ""
    neighbour: str = ""
    city: str = ""
    state: str = ""
    postal_code: str = ""


"""
Valida a unidade da faderação, rem
"""


@validator("state", allow_reuse=True)
async def validate_state(cls, v: Any, **kwargs: int) -> str:
    try:
        return v if StatesEnum(v) else ""

    except ValueError:
        raise ValueError(f"O valor '{v}' não é válido!")
