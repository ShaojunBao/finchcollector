from django.shortcuts import render
from .models import Finch

finches = [
    {
        'name': 'Oliver',
        'breed': 'Gouldian Finch',
        'description': 'Brightly colored with a vibrant personality, known for its green, yellow, and red markings.',
        'age': 2,
    },
    {
        'name': 'Bella',
        'breed': 'Zebra Finch',
        'description': 'Small and easy to care for, with a distinctive black and white striped pattern on its tail.',
        'age': 3,
    },
    {
        'name': 'Charlie',
        'breed': 'Bengalese Finch',
        'description': 'A sociable bird with a pleasant song, known for its spotted and streaked appearance.',
        'age': 1,
    },
    {
        'name': 'Daisy',
        'breed': 'Chaffinch',
        'description': 'A common finch with a strong voice, sporting shades of blue-grey, pinkish-red, and brown.',
        'age': 4,
    },
    {
        'name': 'Milo',
        'breed': 'Greenfinch',
        'description': 'A robust finch with olive-green coloring, known for its playful nature and loud song.',
        'age': 3,
    },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })