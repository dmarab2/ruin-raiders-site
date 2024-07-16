from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, 'mainsite/landing_page.html', {})

def rules_section(request):
    return render(request, 'mainsite/rules_section.html', {})

def basic_mechanics(request):
    return render(request, 'mainsite/basic_mechanics.html', {})