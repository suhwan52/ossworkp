from django import forms

class VoteForm(forms.Form):
    score = forms.IntegerField(min_value=1, max_value=5, label='점수 (1~5)')