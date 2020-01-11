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
    return render(request, 'contact.html')


def sent_info(request):
    user_name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")

    contact_info = Contact(user_name=user_name, email=email, message=message)

    if user_name and email and message:
        contact_info.save()

    return render(request, 'sent_info.html')
