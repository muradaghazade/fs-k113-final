from django.contrib import admin
from core.models import *

admin.site.register([Recipe, Story, Tag, Contact, Subscriber, Category, Comment, RecipeComment])
