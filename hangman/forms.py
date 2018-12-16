from django import forms

def validate_guess(data):
    guess = str(data).strip()
    if len(guess) < 1:
        raise forms.ValidationError("Guess cannot be empty!")
    if not guess.isalpha():
        raise forms.ValidationError(
            "Guess must contain letters only!")


class GuessForm(forms.Form):
    guess = forms.CharField(max_length=20,
                            validators=[validate_guess])

    def __init__(self, *args, **kwargs):
        super(GuessForm, self).__init__(*args, **kwargs)
        self.fields['guess'].label = "Guess a letter or the word:"