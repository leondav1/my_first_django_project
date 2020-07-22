from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request):
    return render(request, 'advertisement/advertisement_list.html', {})


def advertisement_details(request):
    return render(request, 'advertisement/advertisement_details.html', {})
