from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class RegistrationForm(UserCreationForm):
    #email = forms.EmailField(required = True)
    #first_name = forms.CharField(required = False)
    #last_name = forms.CharField(required = False)
    #birtday = forms.DateField(required = False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
