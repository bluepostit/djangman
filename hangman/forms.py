from django import forms

class GuessForm(forms.Form):
    guess = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super(GuessForm, self).__init__(*args, **kwargs)
        self.fields['guess'].label = "Guess a letter or the word:"