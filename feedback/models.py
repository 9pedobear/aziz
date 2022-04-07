from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Feedback(models.Model):# Создаем таблицу
    name = models.CharField(# Поле имен
        verbose_name='ФИО',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков
        blank=True,# Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True# Аргумент для обозначения поля
        # пустым
    )
    question = models.CharField(# Поле имен
        verbose_name='Ваш вопрос',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True# Аргумент для обозначения поля
        # пустым
    )
    phone = models.CharField(# Поле фамилий
        verbose_name='Телефон',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True# Аргумент для обозначения поля
        # пустым
    )
    created = models.DateTimeField(# Поле для даты
        verbose_name='Дата публикации',# Аргумент для альтернативного
        auto_now_add=True,# Аргумент автодобавления даты
        blank=True,# Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    author = models.ForeignKey(# Поле для выбора пользователя
        User,    # Аргумент связи с таблицей
        # содержащий список пользователей
        on_delete=models.CASCADE  # Аргумент для определения как
        # удалять информацию в случае удаления поля
    )

    def get_absolute_url(self):# Метод для получения ссылки на таблицу
        return reverse('view_feedback', kwargs={"pk": self.pk}) # Возвращаем ссылку на таблицу


    def __str__(self):   # Вывод данных в строковом виде
        return f'''{self.author}'''

    class Meta:                           # Расширяем возможность класса
        verbose_name = 'Отзыв'            # Имя таблицы в единственном числе
        verbose_name_plural = 'Отзывы'    # Имя таблицы во множественном числе
        ordering = ['name']               # Сортировка полю имени