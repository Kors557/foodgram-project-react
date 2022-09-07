from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(verbose_name="Название ингредиента", max_length=200)
    measurement_unit = models.CharField(verbose_name="Еденица измерения", max_length=200)

    class Meta:
        ordering = ("name",)
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Tag(models.Model):
    name = models.CharField(verbose_name="Тэг", max_length=200, unique=True)
    color = models.CharField(verbose_name="Цвет в HEX", max_length=7, unique=True)
    slug = models.SlugField(verbose_name="Уникальный слаг", max_length=200, unique=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Recipe(models.Model):
    tags = models.ManyToManyField(Tag, verbose_name="Тег")
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.ManyToManyField(Ingredient, verbose_name="Ингредиенты")
    name = models.CharField(verbose_name="Название", max_length=200)
    image = models.ImageField(verbose_name="Картинка", upload_to="recipes/images/")
    text = models.TextField(verbose_name="Описание")
    cooking_time = models.PositiveIntegerField(
        verbose_name="Время готовки", validators=[MinValueValidator(1, message="Время не может быть меньше 1 мин")]
    )
    pub_date = models.DateField(verbose_name="Дата публикации", auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, verbose_name="Рецепт", on_delete=models.CASCADE, related_name="ingredient_recipe"
    )
    ingredient = models.ForeignKey(
        Ingredient, verbose_name="Ингредиент в рецепте", on_delete=models.CASCADE, related_name="ingredient_recipe"
    )
    amount = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество",
        validators=[MinValueValidator(1, message="Количество не может быть меньше 1 мин")],
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Ингредиент в рецепте"
        verbose_name_plural = "Ингредиенты в рецепте"
        constraints = [models.UniqueConstraint(fields=["recipe", "ingredient"], name="unique ingredient")]


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="favorite_recipe"
    )
    recipe = models.ForeignKey(Recipe, verbose_name="Рецепт", related_name="favorite_recipe", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"


class ShopingList(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="shopping_cart",
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name="Рецепт",
        on_delete=models.CASCADE,
        related_name="shopping_cart",
    )

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"
