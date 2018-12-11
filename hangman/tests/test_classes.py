import datetime

from django.test import TestCase

from ..models import Word

class GameTests(TestCase):
    fixtures = ['words-a-200.json']

    def test_get_words_longer_than_or_equal_length(self):
        word = Word.objects.length__gte(7).order_by('?').first()
        self.assertIsNotNone(word)