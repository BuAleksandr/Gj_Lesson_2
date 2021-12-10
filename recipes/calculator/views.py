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


def recipe(request, dish):
    portion = int(request.GET.get('servings', 1))
    dish = DATA.get(dish)
    menu_portion = {}
    for key, values in dish.items():
        menu_portion[key] = round(values * portion, 2)
    context = {
        'dish': dish,
        'recipe': menu_portion,
    }

    return render(request, 'calculator/index.html', context)

