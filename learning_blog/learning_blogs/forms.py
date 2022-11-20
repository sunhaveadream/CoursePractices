from django import forms

from .models import BlogPost,BlogArtical

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text': ''}

class BlogArticalForm(forms.ModelForm):
    class Meta:
        model = BlogArtical
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}