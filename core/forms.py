from django import forms

class ContactUs(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content = forms.TextField()
