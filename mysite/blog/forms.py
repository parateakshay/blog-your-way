from django.forms import Form
from blog.models import Post,Comment
from django import forms
class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea postcontent'})
            #suppose we want to change the styling of particular field
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs = {'class':"textinputclass"}),
            'text':forms.Textarea(attrs = {'class':'editable medium-editor-textarea'})

        }
