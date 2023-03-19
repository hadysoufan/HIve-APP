from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
