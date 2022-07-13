"""
As enumerações que não precisam estar no banco de dados estão aqui.
"""
from enum import Enum

"""
Lista dos estados brasileiros e suas respectivas siglas.
"""


class StatesBrEnum(str, Enum):
    ac = "Acre"
    al = "Alagoas"
    ap = "Amapá"
    am = "Amazonas"
    ba = "Bahia"
    ce = "Ceará"
    df = "Distrito Federal"
    es = "Espírito Santo"
    go = "Goiás"
    ma = "Maranhão"
    mt = "Mato Grosso"
    ms = "Mato Grosso do Sul"
    mg = "Minas Gerais"
    pa = "Pará"
    pb = "Paraíba"
    pr = "Paraná"
    pe = "Pernambuco"
    pi = "Piauí"
    rj = "Rio de Janeiro"
    rn = "Rio Grande do Norte"
    rs = "Rio Grande do Sul"
    ro = "Rondônia"
    rr = "Roraima"
    sc = "Santa Catarina"
    sp = "São Paulo"
    se = "Sergipe"
    to = "Tocantins"
