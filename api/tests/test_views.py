from django.test import TestCase, Client
from django.urls import reverse_lazy


class UploadIndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('index')
        self.empty_form_data = {'arquivo': ''}
        return super().setUp()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/index.html')

    def test_form_error_empty_file(self):
        response = self.client.post(self.url, self.empty_form_data)
        self.assertFormError(response, 'form', 'arquivo', ['Este campo é obrigatório.'])
        self.assertEquals(response.status_code, 200)


class DetalheLojaViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('detalhe')
        return super().setUp()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/detalhe.html')

    def test_detalhes_in_contexto(self):
        response = self.client.get(self.url)
        self.assertTrue('detalhes' in response.context)
