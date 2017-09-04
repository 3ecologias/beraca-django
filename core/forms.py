# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.conf import settings
from django.template.loader import get_template

class ContactUs(forms.Form):
    name = forms.CharField(required=True,
    widget=forms.TextInput(
    attrs={'class':'input-md round form-control', 'placeholder':'NOME', 'pattern':'.{3,100}', 'id':'name'}))

    email = forms.EmailField(required=True,
    widget=forms.TextInput(
        attrs={'class':'input-md round form-control', 'placeholder':'EMAIL', 'pattern':'.{5,100}', 'id':'email'}))

    content = forms.CharField(required=True,
    widget=forms.Textarea(
        attrs={'class':'input-md round form-control height-84', 'placeholder':'MENSAGEM', 'id':'message'}))

    def send_email(self):
        email_template = get_template('core/email_template.html')
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        message = self.cleaned_data['content']
        context = {
            'name': name,
            'email': from_email,
            'message': message
        }
        html_email = email_template.render(context)
        subject = 'Novo Contato'
        try:
            email = EmailMessage(subject, html_email, from_email,[settings.EMAIL_TO])
            email.content_subtype = "html"
            email.send()
        except BadHeaderError:
            raise ValidationError("Cabeçalho inválido")
