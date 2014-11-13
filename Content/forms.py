from django import forms

class comment_form(forms.Form):
    name = forms.CharField(required= False)
    email = forms.EmailField(required= False)
    content = forms.CharField( required= False)

