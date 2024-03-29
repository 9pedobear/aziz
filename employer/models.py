from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Account(models.Model):# Создаем таблицу
    user = models.ForeignKey(  # Поле для выбора пользователя
        User, # Аргумент связи с таблицей
        on_delete=models.CASCADE # Аргумент для определения как
        # удалять информацию в случае удаления поля
    )
    name = models.CharField( # Поле имен
        verbose_name='Имя', # Аргумент для альтернативного
        # имени поля
        max_length=20 # Аргумент для максимального
        # количества знаков (обязательный)
    )
    second_name = models.CharField( # Поле фамилий
        verbose_name='Фамилия',# Аргумент для альтернативного
        # имени поля
        max_length=20 # Аргумент для максимального
        # количества знаков (обязательный)
    )
    birth_date = models.DateTimeField(# Поле для даты
        verbose_name='Дата рождение', # Аргумент для альтернативного
        # имени поля
        blank=True, # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True # Аргумент для обозначения поля
        # пустым
    )
    def get_absolute_url(self): # Метод для получения ссылки на
        # таблицу
        return reverse('view_account', kwargs={"pk": self.pk}) # Возвращаем ссылку на таблицу

    def __str__(self): # Вывод данных в строковом виде
        return f'''{self.name} -
        '''

    class Meta:  # Расширяем возможность класса
        verbose_name = 'Аккаунт' # Имя таблицы в единственном числе
        verbose_name_plural = 'Аккаунты' # Имя таблицы во множественном
        ordering = ['name'] # Сортировка полю имени


class Employer(models.Model):                # Создаем таблицу с названием
    # Сотрудников
    name = models.CharField(                 # Поле ФИО сотрудников
        verbose_name='ФИО',                  # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True)                           # Аргумент для обозначения поля
        # пустым
    city = models.ForeignKey(                # Поле для выбора города
        'Location',                          # Аргумент связи с таблицей
        # содержащий список городов
        verbose_name='Город',                # Аргумент для альтернативного
        # имени поля
        on_delete=models.CASCADE,            # Аргумент для определения как
        # удалять информацию в случае удаления поля
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True)                           # Аргумент для обозначения поля
        # пустым
    work = models.ManyToManyField(           # Поле для выбора Деятельности
        'Activity',                          # Аргумент связи с таблицей
        verbose_name='Деятельность',         # Аргумент для альтернативного
        # имени поля
        related_name='activity',             # указывает имя обратной связи
        # из модели Activity обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    direction = models.ManyToManyField(      # Поле для выбора Направлений
        'Category',                          # Аргумент связи с таблицей
        verbose_name='Направление',          # Аргумент для альтернативного
        # имени поля
        related_name='category',             # указывает имя обратной связи
        # из модели Category обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    description = models.TextField(          # Поле для ввода Описания
        verbose_name='Описание',             # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True)                           # Аргумент для обозначения поля
        # пустым
    education = models.ManyToManyField(      # Поле для выбора Образования
        'Education',                         # Аргумент связи с таблицей
        verbose_name='Образование',          # Аргумент для альтернативного
        # имени поля
        related_name='education',            # указывает имя обратной связи
        # из модели Education обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    experience = models.CharField(           # Поле для Стажа
        verbose_name='Стаж',                 # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    cabinet = models.ManyToManyField(        # Поле для выбора Кабинета
        'Adress',                            # Аргумент связи с таблицей
        verbose_name='Кабинет',              # Аргумент для альтернативного
        # имени поля
        related_name='adress',               # указывает имя обратной связи
        # из модели Adress обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    personal_consultation = models.CharField(# Поле для назначения Личной
        # встречи
        verbose_name='Личная встреча',       # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    online_consultation = models.CharField(  # Поле для Онлайн-консультация
        verbose_name='Онлайн-консультация',  # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    duration_consultation = models.CharField(# Поле для Длительность консультации
        verbose_name='Длительность консультации', # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    couple_consultation_duration = models.CharField(# Поле для Длительность консультации для пар
        verbose_name='Длительность консультации для пар', # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    photo = models.ImageField(               # Поле для Фото
        verbose_name='Фото',                 # Аргумент для альтернативного
        # имени поля
        upload_to='photos/%Y/%m/%d/',        # Аргумент для указания пути
        # сохранения фото
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    created = models.DateTimeField(          # Поле для даты
        verbose_name='Дата публикации',      # Аргумент для альтернативного
        # имени поля
        auto_now_add=True,                   # Аргумент автодобавления даты
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    updated = models.DateTimeField(          # Поле для выбора города
        verbose_name='Обновлено',            # Аргумент для альтернативного
        # имени поля
        auto_now=True,                       # Аргумент автодобавления даты
        blank=True                           # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    is_published = models.BooleanField(      # Поле для определения
        # опубликованно или нет
        verbose_name='Опубликовано',         # Аргумент для альтернативного
        # имени поля
        default=True,                        # Аргумент для вставки
        # состояния "Опубликовано" по умолчанию
        blank=True                           # Аргумент для обозначения поля
        # не обязательным для заполнения
    )

    def get_absolute_url(self):              # Метод для получения ссылки на
        # таблицу
        return reverse(                      # Возвращаем ссылку на таблицу
            'view_employer',                 # Имя возрвращаемой таблицы
            kwargs={"pk": self.pk}           # Берем из поля id ссылку на
            # таблицу
        )

    def __str__(self):                       # Вывод данных в строковом виде
        return f'''{self.name} -  
        "{self.description}"
        {self.direction} -
        {self.education} -
        {self.experience} лет
        {self.cabinet} -
        {self.personal_consultation} -
        {self.online_consultation} -
        {self.duration_consultation} минут
        {self.couple_consultation_duration} минут
        '''                                  # Обозначаем поля

    class Meta:                              # Расширяем возможность класса
        verbose_name = 'Специалист'          # Имя таблицы в единственном числе
        verbose_name_plural = 'Специалисты'  # Имя таблицы во множественном
        # числе
        ordering = ['name']                  # Сортировка полю имени


class Adress(models.Model):# Создаем таблицу
    cabinet = models.CharField(# Поле с названием кабинета
        verbose_name='Кабинет',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        null=True# Аргумент для обозначения поля
        # пустым
    )

    def get_absolute_url(self):# Метод для получения ссылки на
        # таблицу
        return reverse('view_adress', kwargs={"pk": self.pk})# Возвращаем ссылку на таблицу

    def __str__(self): # Вывод данных в строковом виде
        return f'''{self.cabinet} -
        '''

    class Meta:# Расширяем возможность класса
        verbose_name = 'Адрес'# Имя таблицы в единственном числе
        verbose_name_plural = 'Адреса'# Имя таблицы во множественном
        # числе
        ordering = ['cabinet']# Сортировка полю имени


class Education(models.Model):# Создаем таблицу
    university = models.CharField(# Поле с названием универа
        verbose_name='Университет',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        null=True# Аргумент для обозначения поля
        # пустым
    )
    skill = models.CharField(# Поле с названием навыков
        verbose_name='Квалификация',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        null=True# Аргумент для обозначения поля
        # пустым
    )
    education_date = models.DateTimeField(# Поле с названием года образования
        verbose_name='Год получения',# Аргумент для альтернативного
        # имени поля
        blank=True,# Аргумент для обозначения поля
        null=True# Аргумент для обозначения поля
        # пустым
    )

    def get_absolute_url(self):# Метод для получения ссылки на
        # таблицу
        return reverse('view_education', kwargs={"pk": self.pk})# Вывод данных в строковом виде

    def __str__(self):# Вывод данных в строковом виде
        return f'''{self.university} -
        {self.skill} -
        {self.education_date} -
        '''

    class Meta:# Расширяем возможность класса
        verbose_name = 'Образование'# Имя таблицы в единственном числе
        verbose_name_plural = 'Образования'# Имя таблицы во множественном
        # числе
        ordering = ['university']# Сортировка полю имени


class Category(models.Model):# Создаем таблицу
    direction = models.CharField(# Поле с названием направлений
        'Направление',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        null=True# Аргумент для обозначения поля
        # пустым
    )

    def get_absolute_url(self):# Метод для получения ссылки на
        # таблицу
        return reverse('view_category', kwargs={"pk": self.pk})# Возвращаем ссылку на таблицу

    def __str__(self):# Вывод данных в строковом виде
        return f'''- {self.direction}
        '''

    class Meta:# Расширяем возможность класса
        verbose_name = 'Категория'# Имя таблицы в единственном числе
        verbose_name_plural = 'Категории'# Имя таблицы во множественном
        # числе
        ordering = ['direction']# Сортировка полю имени


class Activity(models.Model):# Создаем таблицу
    work = models.CharField(# Поле с названием деятельности
        'Деятельность',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        null=True# Аргумент для обозначения поля
        # пустым
    )

    def get_absolute_url(self):# Метод для получения ссылки на
        # таблицу
        return reverse('view_activity', kwargs={"pk": self.pk})# Вывод данных в строковом виде

    def __str__(self):# Вывод данных в строковом виде
        return f'''- {self.work}
        '''

    class Meta:# Расширяем возможность класса
        verbose_name = 'Деятельность'# Имя таблицы в единственном числе
        verbose_name_plural = 'Деятельность'# Имя таблицы во множественном
        # числе
        ordering = ['work']# Сортировка полю имени


class Location(models.Model):# Создаем таблицу
    city = models.CharField(# Поле с названием города
        'Город',# Аргумент для альтернативного
        # имени поля
        max_length=1000,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,# Аргумент для обозначения поля
        null=True# Аргумент для обозначения поля
        # пустым
    )

    def get_absolute_url(self):# Метод для получения ссылки на
        # таблицу
        return reverse('view_location', kwargs={"pk": self.pk})# Возвращаем ссылку на таблицу

    def __str__(self):# Вывод данных в строковом виде
        return f'''г. {self.city} 
        '''

    class Meta:# Расширяем возможность класса
        verbose_name = 'Местонахождение'# Имя таблицы в единственном числе
        verbose_name_plural = 'Местонахождения'# Имя таблицы во множественном
        # числе
        ordering = ['city']# Сортировка полю имени


class Application(models.Model):# Создаем таблицу
    employer = models.ForeignKey(# Поле для выбора сотрудников
        Employer,# Аргумент связи с таблицей
        # содержащий список сотрудников
        on_delete=models.CASCADE# Аргумент для определения как
        # удалять информацию в случае удаления поля
    )
    date = models.DateTimeField()# Поле для даты
    category = models.ForeignKey(# Поле для выбора категории
        Category,# Аргумент связи с таблицей
        # содержащий список категорий
        on_delete=models.CASCADE# Аргумент для определения как
        # удалять информацию в случае удаления поля
    )
    author = models.ForeignKey(# Поле для выбора города
        User,# Аргумент связи с таблицей
        on_delete=models.CASCADE# Аргумент для определения как
        # удалять информацию в случае удаления поля
    )
    def __str__(self):# Вывод данных в строковом виде
        return f'{self.employer}'

    class Meta:# Расширяем возможность класса
        verbose_name = 'Заявка'# Имя таблицы в единственном числе
        verbose_name_plural = 'Заявки'# Имя таблицы во множественном
        # числе
        ordering = ['-date']# Сортировка полю имени


class Slider(models.Model):# Создаем таблицу
    image = models.ImageField(# Поле с фото
        upload_to='slider/'# Поле куда загружать
    )
    title = models.CharField(# Поле с названием
        max_length=50# Аргумент для максимального
        # количества знаков (обязательный)
    )
    content = models.CharField(# Поле с названием
        max_length=200,# Аргумент для максимального
        # количества знаков (обязательный)
        blank=True# Аргумент для обозначения поля
    )
    date = models.DateTimeField(# Поле с названием года образования
        auto_now_add=True# Поле автовставкой даты
    )
    def __str__(self):# Вывод данных в строковом виде
        return f'{self.title}'

    class Meta:# Расширяем возможность класса
        verbose_name = 'Слайд'# Имя таблицы в единственном числе
        verbose_name_plural = 'Слайды'# Имя таблицы во множественном
        # числе
        ordering = ['-date']# Сортировка полю имени
