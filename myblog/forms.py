from django import forms
from myblog.models import *


class PostForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'content']
        model = Post

class CommentForm(forms.ModelForm):

    class Meta:
        fields = ['content']
        model = Comment
