from .models import Word

class Game:
    def __init__(self, word=None, guessed_letters=None):
        if word is None:
            self.word = self._find_word()
        else:
            self.word = word
        if guessed_letters is None:
            self.guessed_letters = []
        else:
            self.guessed_letters = guessed_letters

    def _find_word(self):
        word = Word.objects.length__gte(7).order_by('?').first()
        return word

    def get_guessing_string(self):
        guessing = '_' * len(self.word)
        i = 0
        for letter in self.word:
            if letter in self.guessed_letters:
                guessing[i] = self.word[i]
            i += 1
        print('guessing:', guessing)
        return guessing