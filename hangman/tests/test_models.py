import datetime

from django.test import TestCase

from ..models import Word

class WordModelTests(TestCase):
    fixtures = ['words-a-200.json']

    def test_get_words_starting_with(self):
        """Getting words starting with a given string should \
return valid values."""

        search_term = 'a'
        words = Word.objects.filter(word__startswith=search_term)
        self.assertEqual(words.count(), 200)

    def test_get_words_like(self):
        """Getting words like a given string should \
return valid values."""

        search_term = 'ac'
        words = Word.objects.filter(word__icontains=search_term)
        self.assertGreater(words.count(), 0)

    def test_get_words_longer_than_or_equal_length(self):
        """Get words with length greater than or equal to a given \
    length."""

        length = 7
        words = Word.objects.length__gte(length)
        for word in words:
            self.assertGreaterEqual(len(word.word), length)