from django import forms
from posts.models import Post
from ckeditor.widgets import CKEditorWidget

T_or_P = [('Tutor', 'Tutor'), ('Student', 'Student')]

class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    caption = forms.CharField(widget=CKEditorWidget, required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=False)

    class Meta:
        model = Post
        fields = ('subject', 'picture', 'caption', 'tags')




SCHOOL_LEVEL = [('elementary school', 'Elementary School'), ('middle school', 'Middle School'), ('high school', 'High School')]




