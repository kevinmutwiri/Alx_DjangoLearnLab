from django import forms

class ExampleForm(forms.Form):
    """
    A placeholder form created to resolve the 'forms.py' missing error.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
