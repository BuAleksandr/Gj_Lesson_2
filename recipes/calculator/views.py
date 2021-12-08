from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    portion = int(request.GET.get('servings', 1))
    menu_portion = {}
    for key, values in DATA.items():
        if key == 'omlet':
            for i in values:
                menu_portion[i] = values[i] * portion
    context = {
        'recipe': menu_portion,
    }

    return render(request, 'calculator/index.html', context)


def pasta(request):
    portion = int(request.GET.get('servings', 1))
    menu_portion = {}
    for key, values in DATA.items():
        if key == 'pasta':
            for i in values:
                menu_portion[i] = values[i] * portion
    context = {
        'recipe': menu_portion,
    }

    return render(request, 'calculator/index.html', context)


def buter(request):
    portion = int(request.GET.get('servings', 1))
    menu_portion = {}
    for key, values in DATA.items():
        if key == 'buter':
            for i in values:
                menu_portion[i] = values[i] * portion
    context = {
        'recipe': menu_portion,
    }

    return render(request, 'calculator/index.html', context)
