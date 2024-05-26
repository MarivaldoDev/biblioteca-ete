from django.shortcuts import render

# Create your views here.
def first(requests):
    return render(requests, 'first.html')