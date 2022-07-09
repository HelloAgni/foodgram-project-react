from django.urls import include, path
from rest_framework import routers
from .views import (IngredientViewSet, RecipeViewSet,
                    TagViewSet, CustomUserViewSet)

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('recipes', RecipeViewSet)
router.register('ingredients', IngredientViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
