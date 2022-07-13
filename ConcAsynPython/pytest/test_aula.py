# coding=utf-8
import unittest

"""
Teste para verificar retorno de status code 200 - OK
"""


class StarWarsGatewaySWAPITests(unittest.TestCase):
    def setUp(self):
        self.dados_starwars_gateway = StarWarsGatewaySWAPI()

    def test_obtem_resposta_do_servidor(self):
        resposta = self.dados_starwars_gateway.buscar_dados()

        self.assertEqual(200, resposta.status_code)

assert isinstance()

"""
Para buscar de api externa 
"""

# coding=utf-8
import requests


class StarWarsGatewaySWAPI(object):
    URL = 'http://swapi.co/api/'

    def buscar_dados(self):
        return requests.get(self.URL)


"""
Buscando por nome
"""


# [...] StarWarsGatewaySWAPITests
def test_obtem_personagem(self):
    resposta = self.dados_star_wars_gateway.buscar_personagem(nome='Anakin')

    self.assertEqual(200, resposta.status_code)
    conteudo = resposta.json()
    # results é uma lista, pegamos o nome do primeiro resultado
    self.assertEqual('Anakin Skywalker', conteudo['results'][0]['name'])


# coding=utf-8
import requests
from urllib import urlencode


class StarWarsGatewaySWAPI(object):
    URL = 'http://swapi.co/api/'

    def buscar_dados(self):
        return requests.get(self.URL)

    def buscar_personagem(self, nome):
        recurso = 'people/?'
        # traduz nosso dicionário python nos parametros de busca HTTP
        parametros_de_busca = urlencode({'search': nome})

        url_completa = self.URL + recurso + parametros_de_busca

        return requests.get(url_completa)


"""
Utilizando mock
"""
# coding=utf-8
import unittest
import requests
import mock
from star_wars.starwars_gateway_swapi import StarWarsGatewaySWAPI


class StarWarsGatewaySWAPITests(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock(spec=requests)  # 1
        self.dados_star_wars_gateway = StarWarsGatewaySWAPI(self.client)

    def test_obtem_resposta_do_servidor(self):
        self.client.get.return_value = mock.Mock(status_code=200)  # 2

        resposta = self.dados_star_wars_gateway.buscar_dados()

        self.assertEqual(200, resposta.status_code)

    def test_obtem_personagem(self):
        retorno_json = {  # 3
            'count': 1,
            'results': [
                {'name': 'Anakin Skywalker'}
            ]
        }
        mock_response = mock.Mock(status_code=200)  # 4
        mock_response.json.return_value = retorno_json
        self.client.get.return_value = mock_response

        resposta = self.dados_star_wars_gateway.buscar_personagem(nome='Anakin')

        conteudo = resposta.json()
        self.assertEqual('Anakin Skywalker', conteudo['results'][0]['name'])
        # 5
        self.client.get.assert_called_with('http://swapi.co/api/people/?search=Anakin')


"""
Excecao de personagem nao encontrado
"""
# coding=utf-8
class PersonagemNaoEncontradoException(Exception):
    def __init__(self, nome):
        message = 'Personagem {} não encontrado'.format(nome)
        super(PersonagemNaoEncontradoException, self).__init__(message)


# coding=utf-8
from urllib import urlencode
from star_wars.exceptions import PersonagemNaoEncontradoException

# [...] StarWarsGatewaySWAPI

    def buscar_personagem(self, nome):
        recurso = 'people/?'
        parametros_de_busca = urlencode({'search': nome})

        url_completa = self.URL + recurso + parametros_de_busca

        response = self.client.get(url_completa)
        conteudo = response.json()

        if conteudo['count'] == 0:
            raise PersonagemNaoEncontradoException(nome)
        return response
