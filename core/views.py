from django.shortcuts import render, redirect
from core.models import *
from core.forms import *
from django.views.generic import UpdateView, ListView
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


class StoriesView(ListView):
    model = Story
    template_name = 'stories.html'
    context_object_name = 'stories'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        search = self.request.GET.get('search')
        queryset = Story.objects.order_by('-id')
        if tag:
            queryset = Story.objects.filter(tag__title=tag).order_by('-id')
        if cat:
            queryset = Story.objects.filter(category__title=cat).order_by('-id')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset


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