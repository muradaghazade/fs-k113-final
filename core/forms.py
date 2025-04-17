from django import forms 
from core.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email' }),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Comment'}),
        }


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Comment'}),
        }


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'description', 'image', 'text', 'category', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image', 'text', 'category', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
        }