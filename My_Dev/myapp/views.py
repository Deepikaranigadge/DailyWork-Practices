from django.shortcuts import render

def home(request):
    data = {
        'name': 'Deepika',
        'role': 'Django Developer'
    }
    return render(request, 'home.html', data)

