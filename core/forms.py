# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail, BadHeaderError

class ContactUs(forms.Form):
    name = forms.CharField(required=True,
    widget=forms.TextInput(
    attrs={'class':'input-md round form-control', 'placeholder':'NOME', 'pattern':'.{3,100}', 'id':'name'}))

    email = forms.EmailField(required=True,
    widget=forms.TextInput(
        attrs={'class':'input-md round form-control', 'placeholder':'EMAIL', 'pattern':'.{5,100}', 'id':'email'}))

    content = forms.CharField(required=True,
    widget=forms.Textarea(
        attrs={'class':'input-md round form-control', 'style':'height: 84px;', 'placeholder':'MENSAGEM', 'id':'message'}))

    def send_email(self):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        message = self.cleaned_data['content']
        subject = 'Novo Contato'
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            raise ValidationError("Cabeçalho inválido")
