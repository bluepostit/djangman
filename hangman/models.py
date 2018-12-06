from django.db import models

class Word(models.Model):
    word = models.TextField(max_length=40, unique=True)

    def __str__(self):
        return self.word

    def __repr__(self):
        return f"<Word: {self.word}"
