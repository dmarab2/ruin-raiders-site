from django.shortcuts import render
from .models import Bounty

# Create your views here.

def landing_page(request):
    return render(request, 'mainsite/landing_page.html', {})

def rules_section(request):
    return render(request, 'mainsite/rules_section.html', {})

def basic_mechanics(request):
    return render(request, 'mainsite/basic_mechanics.html', {})

def bounty_list(request):
    bounties = Bounty.objects.all()
    return render(request, 'mainsite/bounty_list.html', {'bounties': bounties})