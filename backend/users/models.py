from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    first_name = models.CharField("Имя", max_length=150)
    username = models.CharField("Имя пользователя", max_length=150, unique=True)
    last_name = models.CharField("Фамилия", max_length=150)
    email = models.EmailField("Адрес электронной почты", max_length=254, unique=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        related_name="follower",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User, verbose_name="Автор", related_name="following", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "user",
                    "author",
                ),
                name="unique_subscribe",
            ),
        )
