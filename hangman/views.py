from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from hangman.hangman import Game
from .forms import GuessForm

def index(request):
    game_dict = request.session.get('game', None)
    game = Game(
        game_dict['word'],
        game_dict['guessed_letters'],
        game_dict['guesses']
    )
    print(game)
    game_dict['guessing_string'] = game.get_guessing_string()

    context = {
        'game': game_dict,
    }
    if not game.has_guessed_word:
        context['form'] = GuessForm()
    return render(request, 'index.html', context)

def new_game(request):
    game = Game()
    request.session['game'] = {
        'word': str(game.word),
        'guessed_letters': [],
        'guesses': 0,
    }
    return redirect(reverse('hangman:index'))

def guess(request):
    form = GuessForm(request.POST)
    if form.is_valid():
        guess = form.cleaned_data['guess']
        game_dict = request.session.get('game', None)
        game = Game(game_dict['word'], game_dict['guessed_letters'])
        if len(guess) == 1:
            valid_guess = game.guess_letter(guess)
        else:
            valid_guess = game.guess_word(guess)

        request.session['game'] = {
            'word': str(game.word),
            'guessed_letters': game.guessed_letters,
            'guesses': game.count_guesses,
            'has_guessed_word': game.has_guessed_word,
        }
    elif form.errors:
        for error in form.errors['guess']:
            messages.error(request, str(error))
    return redirect(reverse('hangman:index'))