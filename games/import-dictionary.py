import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from django.contrib.auth.models import User

from hangman.models import Word

WORDS_FILE_PATH = "../sowpods.txt"
def load_words_file():
    with open(WORDS_FILE_PATH) as f:
        words = [word.strip().lower() for word in f]
        return words

def load_words_file_selective():
    word_count = 0
    word_limit = 200
    words = []
    with open(WORDS_FILE_PATH) as f:
        for word in f:
            words.append(word.strip().lower())
            word_count += 1
            if word_count >= word_limit:
                break
    return words

def save_words_to_models(words: list):
    word_objects = [Word(word=word) for word in words]
    Word.objects.bulk_create(word_objects)

if __name__ == '__main__':
    words = load_words_file()
    #words = load_words_file_selective()
    print(f"There are {len(words)} words")
    save_words_to_models(words)