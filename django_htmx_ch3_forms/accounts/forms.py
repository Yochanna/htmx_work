from django import forms
from django.contrib.auth.models import User

class SignupStepOneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {"password": forms.PasswordInput()}

class SignupStepTwoForm(forms.Form):
    bio = forms.CharField(widget=forms.Textarea, required=True)
    avatar = forms.ImageField(required=False)
