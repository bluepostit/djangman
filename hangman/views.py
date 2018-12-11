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
