from django.db import models
from accounts.models import User

#Recipe, User, Story Comment Category, Tag, Contact, Subscriber

class Story(models.Model):
    user = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='files/')
    text = models.TextField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', related_name='stories' , on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='stories', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    user = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='files/')
    text = models.TextField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', related_name='recipes' , on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='recipes', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    story = models.ForeignKey('Story', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text
    

class RecipeComment(models.Model):
    user = models.ForeignKey(User, related_name='recipe_comments', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey('Recipe', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text
    

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='files/')

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email