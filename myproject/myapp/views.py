from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Nandita',
        'age': 19,
        'nationality': 'Indian',
    
    }
    return render(request, 'index.html', context)