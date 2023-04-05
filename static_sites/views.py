from django.shortcuts import render
from django.contrib.auth.views import LoginView


def show_legal_page(request):
    return render(request, 'static_sites/legal.html')


def show_about_page(request):
    return render(request, 'static_sites/about.html')


def show_landing_page(request):
    return render(request, 'static_sites/index.html')


def show_projects_page(request):
    return render(request, 'static_sites/projects.html')

class AdminLogin(LoginView):
    template_name = 'static_sites/admin_login.html'


def show_example_pages(request):
    return render(request, 'static_sites/example_pages.html')


def show_contact_page(request):
    return render(request, 'static_sites/contact.html')