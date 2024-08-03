from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from django.http import HttpResponseRedirect
'''from .forms import ContactFormForm'''
from .forms import ContactFormModelForm

# Create your views here.

def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

def about(request):
    return render(request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})


'''def contact(request):
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
'''
def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito/')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')
