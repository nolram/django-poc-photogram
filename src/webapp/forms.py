from .models import Post, Like

from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'photo']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['post']