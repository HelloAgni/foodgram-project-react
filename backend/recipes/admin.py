from django.contrib import admin

from .models import Ingredient, IngredientAmount, Recipe, Tag


class IngredientAmountAdmin(admin.TabularInline):
    model = IngredientAmount
    autocomplete_fields = ('ingredient',)


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountAdmin,)
    list_display = (
        'id', 'name', 'author', 'text', 'pub_date'
    )
    search_fields = ('name', 'author', 'tags')
    list_filter = ('name', 'author', 'tags', 'pub_date')
    filter_vertical = ('tags',)
    empy_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'measurement_unit'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empy_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'color', 'slug'
    )
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    empy_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
