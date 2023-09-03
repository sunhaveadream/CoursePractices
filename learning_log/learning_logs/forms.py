from django import forms

from .models import Topic,Entry,Teacher,TeacherMessage

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name']
        labels = {'name': ''}


class TeacherMessageForm(forms.ModelForm):
    class Meta:
        model = TeacherMessage
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}