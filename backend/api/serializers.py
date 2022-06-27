from recipes.models import Ingredient, Recipe, Tag, IngredientAmount
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name', 'last_name',        
        )


class IngrediendAmountSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(
    id = serializers.ReadOnlyField(
        source='ingredient.id',
    )    
    # name = serializers.CharField(
    name = serializers.ReadOnlyField(
        source='ingredient.name',
    )
    # measurement_unit = serializers.CharField(
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit',
    )
    class Meta:
        model = IngredientAmount
        fields = ('id', 'name', 'measurement_unit', 'amount')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngrediendAmountSerializer(
        source='recipes',
        many=True,
    )
    tags = TagSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    class Meta:
        model = Recipe
        fields = ('id', 'tags', 'author', 'ingredients', 'name', 'image', 'text', 'cooking_time')
        # depth = 5


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'





