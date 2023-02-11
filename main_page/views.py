from django.shortcuts import render, redirect
from .models import Category, Dish
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required, user_passes_test



def is_manager(user):
    return user.groups.filter(name='manager').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def main(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specials = Dish.objects.filter(is_visible=True, is_special=True)
    form_reserve = ReservationForm()

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'specials': specials,
        'form_reserve': form_reserve
    })