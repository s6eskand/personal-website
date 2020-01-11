from django.shortcuts import render
from .models import Contact


# Create your views here.
def warning(request):
    return render(request, 'warning.html')


def home(request):
    return render(request, 'base.html')


def navigation(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def projects(request):
    return render(request, 'projects.html')


def claw_machine(request):
    return render(request, 'claw_machine.html')


def coollistings(request):
    return render(request, 'coollistings.html')


def wheel_of_fortune(request):
    return render(request, 'wof.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    search = request.POST.get('search')
    Contact.objects.create(contact=contact)

    return render(request, 'contact.html')
