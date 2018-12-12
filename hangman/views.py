from django.shortcuts import redirect, render, reverse
from hangman.hangman import Game

def index(request):
    game_dict = request.session.get('game', None)
    game = Game(game_dict['word'], game_dict['guessed_letters'])
    game_dict['guessing_string'] = game.get_guessing_string()
    return render(request, 'index.html', {
        'game': game_dict,
    })

def new_game(request):
    game = Game()
    request.session['game'] = {
        'word': str(game.word),
        'guessed_letters': []
    }
    return redirect(reverse('hangman:index'))

def guess(request):
    guess = request.POST.get('guess', None)
    if guess is not None:
        game_dict = request.session.get('game', None)
        game = Game(game_dict['word'], game_dict['guessed_letters'])
        if len(guess) == 1:
            game.guess_letter(guess)
        else:
            game.guess_word(guess)

        request.session['game'] = {
            'word': str(game.word),
            'guessed_letters': game.guessed_letters,
            'has_guessed_word': game.has_guessed_word,
        }
    return redirect(reverse('hangman:index'))