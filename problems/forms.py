from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'class': 'code-editor'}))

# Comment