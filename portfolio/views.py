from django.shortcuts import render


# Create your views here.
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
