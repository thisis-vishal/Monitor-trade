from django import forms

class Stock(forms.Form):
    Symbol = forms.CharField(label='Stock Symbol', max_length=100)