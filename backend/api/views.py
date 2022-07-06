from recipes.models import Ingredient, Recipe, Tag
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
from users.models import User

from .serializers import (IngredientSerializer, RecipeEditSerializer,
                          RecipeReadSerializer, TagSerializer,
                          UserCreatSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserSerializer
        return UserCreatSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeReadSerializer
        return RecipeEditSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
