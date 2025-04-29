from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home , name='home'),
    path('story/<int:id>/', story_detail , name='story_detail'),
    path('stories/', StoriesView.as_view() , name='stories'),
    path('about/', about , name='about'),
    path('contact/', contact , name='contact'),
    path('recipes/', recipes, name='recipes'),
    path('recipe/<int:id>/', recipe_detail, name='recipe_detail'),
    path('create_story', create_story, name='create_story'),
    path('create_recipe', create_recipe, name='create_recipe'),
    path('edit_story/<int:pk>/', EditStory.as_view(), name='edit_story'),
]