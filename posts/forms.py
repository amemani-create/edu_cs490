from django import forms
from posts.models import Post
from ckeditor.widgets import CKEditorWidget


class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    caption = forms.CharField(widget=CKEditorWidget, required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=False)

    class Meta:
        model = Post
        fields = ('subject', 'picture', 'caption', 'tags')


VIDEO_OR_PERSON = [('Video', 'Video'), ('In Person', 'In Person'), ('Both', 'Both')]

SCHOOL_LEVEL = [('elementary school', 'Elementary School'), ('middle school', 'Middle School'), ('high school', 'High School')]




