from django.contrib import admin
from django.db.models import Count

from .models import (FavoriteRecipe, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Subscribe, Tag)


class IngredientAmountAdmin(admin.TabularInline):
    model = IngredientAmount
    autocomplete_fields = ('ingredient',)


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountAdmin,)
    list_display = (
        'id', 'name', 'author', 'text', 'pub_date', 'favorite_count'
    )
    search_fields = ('name', 'author', 'tags')
    list_filter = ('name', 'author', 'tags', 'pub_date')
    filter_vertical = ('tags',)
    empy_value_display = '-пусто-'

    def favorite_count(self, obj):
        return obj.obj_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            obj_count=Count("favorite_recipe", distinct=True),
        )


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


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'favorite_recipe'
    )
    search_fields = ('favorite_recipe',)
    list_filter = ('id', 'user', 'favorite_recipe')
    empy_value_display = '-пусто-'


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'author', 'user', 'created'
    )
    search_fields = ('author', 'created')
    list_filter = ('author', 'user', 'created')
    empy_value_display = '-пусто-'


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'recipe'
    )
    search_fields = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    empy_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(FavoriteRecipe, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
