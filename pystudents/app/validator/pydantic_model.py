from datetime import datetime

from pydantic import BaseModel, validator

"""
 Estrutura de exemplo para armazenar pedido.
"""


class Order(BaseModel):
    id: int
    name: str


"""
Estruturar de exemplo para armazenar o pedido (com validação)
"""


class ValidatedOrder(Order):
    value: float
    order_date: datetime


"""
Verifica se a ordem do pedido não está no futuro.
"""


@validator("order_date")
async def validate_order(cls, v: datetime, **kwargs) -> datetime:
    if v > datetime.now():
        raise ValueError("A data do pedido não pode estar no futuro!")

    return v


"""
Verifica se o valor do pedido não é menor ou igual a zero.
"""


@validator("value")
async def validate_value(cls, v: float, **kwargs) -> float:
    if v <= 0.0:
        raise ValueError(
            "Valor do pedido não pode ser menor ou igual a zero!"
        )

    return v
