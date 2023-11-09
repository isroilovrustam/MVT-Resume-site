from django.shortcuts import render, redirect
from .models import About, Blog, Category, Tag, Comment, Collection, Contact
from .forms import ContactForm, CommentForm, NewslatterForm

# Create your views here.


def indexView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    ctx = {
        'about': about,
        'collections': collection,
    }
    return render(request, 'index.html', ctx)


def collectionView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')
    ctx = {
        'about': about,
        'collections': collection,
    }
    return render(request, 'collection.html', ctx)


def aboutView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:5]
    ctx = {
        'about': about,
        'collections': collection,
    }
    return render(request, 'about.html', ctx)


def serviceView(request):
    about = About.objects.all()
    ctx = {
        'about': about,
    }
    return render(request, 'services.html', ctx)


def blogView(request):
    about = About.objects.all()
    blog = Blog.objects.all().order_by('-id')
    popular = Blog.objects.all().order_by('-id')[:3]
    category = Category.objects.all()
    tag = Tag.objects.all()
    form = NewslatterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    ctx = {
        'about': about,
        'blogs': blog,
        'category': category,
        'tag': tag,
        'popular': popular,
        'form': form
    }
    return render(request, 'blog.html', ctx)


def detailView(request, pk):
    detail = Blog.objects.get(id=pk)
    about = About.objects.all()
    popular = Blog.objects.all().order_by('-id')[:3]
    category = Category.objects.all()
    tag = Tag.objects.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = detail
        com.save()
        return redirect('.')
    formnew = NewslatterForm(request.POST or None)
    if formnew.is_valid():
        formnew.save()
        return redirect('.')
    ctx = {
        'form': form,
        'detail': detail,
        'about': about,
        'popular': popular,
        'category': category,
        'tag': tag,
        'formnew': formnew
    }
    return render(request, 'single.html', ctx)


def contactView(request):
    about = About.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    ctx = {
        'about': about,
        'form': form
    }
    return render(request, 'contact.html', ctx)
