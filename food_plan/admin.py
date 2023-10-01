from django.contrib import admin
from food_plan.models import (Client, MealPlan, FoodList,
                              Foodstuff, Recipe, Transaction)
from django.utils.html import format_html

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('menu_type', 'is_free', 'text', 'cooking_time', 'calories',
                    'fats', 'proteins', 'carbs', 'image', 'preview_image')
    readonly_fields = ('preview_image',)
    list_display = ['menu_type', 'cooking_time', 'calories',
                    'fats', 'proteins', 'carbs']
    def preview_image(self, obj):
        return format_html('<img src="{}" height="200"/>',
                           obj.image.url)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'subscription',
                    'subscription_expiration_date']
    readonly_fields = ['user']


@admin.register(FoodList)
class FoodListAdmin(admin.ModelAdmin):
    pass


@admin.register(Foodstuff)
class FoodstuffAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'weight', 'category']


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ['client', 'menu_type',
                    'number_persons', 'calories']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'date']
