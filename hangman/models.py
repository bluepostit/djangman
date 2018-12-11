from django.db import models
from django.db.models.functions import Length

class WordManager(models.Manager):
    def length__gte(self, length):
        return self.annotate(word_len=Length('word')) \
            .filter(word_len__gte=length)

class Word(models.Model):
    word = models.TextField(max_length=40, unique=True)
    objects = WordManager()

    def __str__(self):
        return self.word

    def __repr__(self):
        return f"<Word: {self.word}>"
