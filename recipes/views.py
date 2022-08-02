from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })


def recipes(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })
