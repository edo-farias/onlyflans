from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan, ContactForm, Comment
from django.http import HttpResponseRedirect
from .forms import ContactFormForm, CommentForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 


# Create your views here.

def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  
        else:
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    return render(request, 'login.html')


@login_required
def flan_detail(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    comments = flan.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.flan = flan
            comment.user = request.user
            comment.save()
            return redirect('flan_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'flan_detail.html', {
        'flan': flan,
        'comments': comments,
        'comment_form': comment_form
    })