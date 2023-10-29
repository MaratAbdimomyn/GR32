from django import forms
from captcha.fields import CaptchaField

class SearchForm(forms.Form):
    name = forms.CharField(label="Введите название модели")
    captcha = CaptchaField()