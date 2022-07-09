from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from recipes.models import Ingredient, Recipe, Tag
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated

from .serializers import (IngredientSerializer, RecipeEditSerializer,
                          RecipeReadSerializer, SetPasswordSerializer,
                          TagSerializer, UserCreateSerializer,
                          UserListSerializer)

User = get_user_model()


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


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'set_password':
            return SetPasswordSerializer
        if self.action == 'create':
            return UserCreateSerializer
        return UserListSerializer
