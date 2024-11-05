from django import forms
from .models import Blog_post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['name','username','post','disc']
    


    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter name'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['post'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter post'})
        self.fields['disc'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter description'})