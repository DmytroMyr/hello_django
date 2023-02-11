from django.contrib import admin
from .models import Category, Dish, About, WhyUs, Events, Reservation


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishAdmin]
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']


@admin.register(Dish)
class AllDishAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'description', 'price', 'photo', 'category', 'is_special']
    list_editable = ['position', 'is_visible', 'price', 'photo', 'category', 'is_special']
    list_filter = ['category', 'is_special', 'is_visible']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display = ['title', 'paragraph', 'video']
    list_editable = ['paragraph', 'video']

@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    model = WhyUs
    list_display = ['title', 'position', 'paragraph']
    list_editable = ['position', 'paragraph']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    model = Events
    list_display = ['title', 'position', 'price', 'description', 'photo']
    list_editable = ['position', 'price', 'description', 'photo']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['name', 'is_processed']
