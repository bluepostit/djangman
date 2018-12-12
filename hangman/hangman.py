from .models import Word

class Game:
    def __init__(self, word=None, guessed_letters=[]):
        self.has_guessed_word = False
        self.guessed_letters = []
        if word is None:
            self.word = self._find_word()
        else:
            self.word = word
            if len(guessed_letters) > 0:
                self.guessed_letters = guessed_letters
                self._check_for_guessed_word()

    def _find_word(self):
        word = Word.objects.length__gte(7).order_by('?').first()
        return word

    def guess_letter(self, letter):
        self.guessed_letters.append(letter)
        self._check_for_guessed_word()

    def guess_word(self, word):
        if self.word.lower() == word.trim().lower():
            self.has_guessed_word = True

    def _check_for_guessed_word(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                break
        else:
            self.has_guessed_word = True

    def get_guessing_string(self):
        guessing = ['_' for ch in self.word]
        i = 0
        for letter in self.word:
            if letter in self.guessed_letters:
                guessing[i] = self.word[i]
            i += 1
        print('guessing:', guessing)
        return ' '.join(guessing)