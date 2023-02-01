from django.shortcuts import render
from .models import Category

def main(request):
    categories = Category.objects.filter(is_visible=True)

    return render(request, 'menu.html', context={
        'categories': categories
    })