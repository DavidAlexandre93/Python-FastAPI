# coding=utf-8
# Desenvolvimento Aberto
# TestParticipante.py

from unittest import TestCase

__author__ = 'Desenvolvimento Aberto'


class TestParticipante(TestCase):

    # Define Métodos de Testes

    def test_setNome(self):
        # Testa métodos Getter e Setter
        p1 = Participante()
        p1.setNome("Nome")
        self.assertEqual("Nome", p1.getNome())

    def test_setIdade(self):
        # Testa métodos Getter e Setter
        p2 = Participante()
        p2.setIdade(20)
        self.assertEqual(20, p2.getIdade())
