from django.test import Client, TestCase

class IndexPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get('/hangman/')
        self.assertEqual(response.status_code, 200)

class NewGameTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_new_game_url(self):
        response = self.client.get('/hangman/new/')
        self.assertRedirects(response, '/hangman/')

