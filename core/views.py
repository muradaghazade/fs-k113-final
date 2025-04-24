from django.shortcuts import render, redirect
from core.models import *
from core.forms import *
from django.views.generic import UpdateView
from django.urls import reverse_lazy


def home(request):
    stories = Story.objects.order_by('-id')
    categories = Category.objects.all()
    new_story = stories.first()
    holiday_stories = stories.filter(category__title='Holiday').order_by('-id')
    context = {
        'stories': stories,
        'new_story': new_story,
        'categories': categories,
        'holiday_stories': holiday_stories
    }
    return render(request, 'index.html', context)


def story_detail(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.story = Story.objects.get(id=id)
            comment.save()
            return redirect('core:story_detail', id=id)
    story = Story.objects.get(id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_stories = Story.objects.order_by('-id')[:3]
    form = CommentForm()
    context = {
        'story': story,
        'categories': categories,
        'tags': tags,
        'recent_stories': recent_stories,
        'form':form
    }
    return render(request, 'single.html', context)


def stories(request):
    stories = Story.objects.order_by('-id')



    tag = request.GET.get('tag')
    if tag:
        stories = Story.objects.filter(tag__title=tag).order_by('-id')



        
    cat = request.GET.get('cat')
    if cat:
        stories = Story.objects.filter(category__title=cat).order_by('-id')
    search = request.GET.get('search')
    if search:
        stories = stories.filter(title__icontains=search)
    categories = Category.objects.all()
    context = {
        'stories': stories,
        'categories': categories,
    }
    return render(request, 'stories.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('salam')
            form.save()
            return redirect('core:home')
    form=ContactForm()
    return render(request, 'contact.html', {'form': form})


def recipes(request):
    recipes = Recipe.objects.order_by('-id')
    search = request.GET.get('search')
    if search:
        recipes = recipes.filter(title__icontains=search)
    categories = Category.objects.all()
    context = {
        'recipes': recipes,
        'categories': categories,
    }
    return render(request, 'recipes.html', context)


def recipe_detail(request, id):
    if request.method == 'POST':
        form = RecipeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.recipe = Recipe.objects.get(id=id)
            comment.save()
            return redirect('core:recipe_detail', id=id)
    form = RecipeCommentForm()
    recipe = Recipe.objects.get(id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_recipes = Recipe.objects.order_by('-id')[:3]
    context = {
        'story': recipe,
        'categories': categories,
        'tags': tags,
        'recent_stories': recent_recipes,
        'form':form,
    }
    return render(request, 'single.html', context)


def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save()
            story.user = request.user
            story.save()
            return redirect('core:home')
    form = StoryForm()
    context = {
        'form': form
    }
    return render(request, 'create_story.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            recipe.user = request.user
            recipe.save()
            return redirect('core:home')
    form = RecipeForm()
    context = {
        'form': form
    }
    return render(request, 'create_recipe.html', context)


class EditStory(UpdateView):
    model = Story
    form_class = StoryForm
    template_name = 'edit-story.html'
    
    def get_success_url(self):
        return reverse_lazy('accounts:user_profile', kwargs = {'id': self.request.user.id})