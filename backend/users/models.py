from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name='электронная почта'
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='имя пользователя'
    )
    password = models.CharField(max_length=150, verbose_name='пароль')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):

    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name='подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authors',
        verbose_name='автор'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        constraints = [
            models.UniqueConstraint(fields=['subscriber', 'author'],
                                    name='unique_subscribe')
        ]

    def __str__(self):
        return f'{self.subscriber} - {self.author}'
