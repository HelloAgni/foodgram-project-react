from drf_extra_fields.fields import Base64ImageField
from recipes.models import Ingredient, IngredientAmount, Recipe, Tag
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name', 'last_name',
        )


class IngrediendAmountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(
        source='ingredient.id',
    )
    name = serializers.ReadOnlyField(
        source='ingredient.name',
    )
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


class RecipeReadSerializer(serializers.ModelSerializer):
    ingredients = IngrediendAmountSerializer(
        many=True,
        source='recipe',
        required=True,
        )
    tags = TagSerializer(
        many=True,
        read_only=True
        )
    author = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients',
            'name', 'image', 'text', 'cooking_time'
            )
        # depth = 5


class IngredientsEditSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = Ingredient
        fields = ('id', 'amount')


class RecipeEditSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None,
        use_url=True)
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
        )
    ingredients = IngredientsEditSerializer(
        many=True)

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('author',)

    def validate(self, data):
        name = data['name']
        if len(name) < 4:
            raise serializers.ValidationError(
                    'Название рецепта минимум 4 символа')
        ingredients = data['ingredients']
        ingredients_list = []
        for items in ingredients:
            if items['id'] in ingredients_list:
                raise serializers.ValidationError(
                    'Ингредиенты не должны повторяться!')
            ingredients_list.append(items['id'])
        tags = data['tags']
        if not tags:
            raise serializers.ValidationError(
                'Укажите минимум один Тэг')
        cooking_time = data['cooking_time']
        if cooking_time > 500 or cooking_time < 1:
            raise serializers.ValidationError(
                'Проверьте время приготовления блюда'
                )
        return data

    def create_ingredients(self, ingredients, recipe):
        for ingredient in ingredients:
            IngredientAmount.objects.create(
                recipe=recipe,
                ingredient_id=ingredient.get('id'),
                amount=ingredient.get('amount'), )

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        self.create_ingredients(ingredients, recipe)
        return recipe

    def update(self, instance, validated_data):
        if 'ingredients' in validated_data:
            ingredients = validated_data.pop('ingredients')
            instance.ingredients.clear()
            self.create_ingredients(ingredients, instance)
        if 'tags' in validated_data:
            instance.tags.set(
                validated_data.pop('tags'))
        return super().update(
            instance, validated_data)

    def to_representation(self, instance):
        return RecipeReadSerializer(
            instance,
            context={
                'request': self.context.get('request')
            }).data


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
