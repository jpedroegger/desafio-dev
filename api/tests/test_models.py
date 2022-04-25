from django.test import TestCase

from api.models import Transacao


class OperationModelTestCase(TestCase):
    def setUp(self):
        self.transacoes = Transacao.objects.all()

    def test_tipo_de_transacao(self):
        field = Transacao._meta.get_field('tipo')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)

    def test_data_transacao(self):
        field = Transacao._meta.get_field('data')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)

    def test_valor_transacao(self):
        field = Transacao._meta.get_field('valor')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertEquals(field.max_digits, 10)
        self.assertEquals(field.decimal_places, 2)

    def test_cpf_transacao(self):
        field = Transacao._meta.get_field('cpf')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertEquals(field.max_length, 11)

    def test_cartao_transacao(self):
        field = Transacao._meta.get_field('cartao')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertEquals(field.max_length, 12)

    def test_dono_da_loja(self):
        field = Transacao._meta.get_field('dono')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertEquals(field.max_length, 14)

    def test_nome_da_loja(self):
        field = Transacao._meta.get_field('loja')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertEquals(field.max_length, 19)
