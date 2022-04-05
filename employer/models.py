from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Account(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Имя',
        max_length=20
    )
    second_name = models.CharField(
        verbose_name='Фамилия',
        max_length=20
    )
    birth_date = models.DateTimeField(
        verbose_name='Дата рождение',
        blank=True,
        null=True
    )
    def get_absolute_url(self):
        return reverse('view_account', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''{self.name} -
        '''

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
        ordering = ['name']


class Employer(models.Model):
    name = models.CharField(
        verbose_name='ФИО',
        max_length=1000,
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        'Location',
        verbose_name='Город',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    work = models.ManyToManyField(
        'Activity',
        verbose_name='Деятельность',
        related_name='activity',
        blank=True,
    )
    direction = models.ManyToManyField(
        'Category',
        verbose_name='Направление',
        related_name='category',
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=1000,
        blank=True,
        null=True)
    education = models.ManyToManyField(
        'Education',
        verbose_name='Образование',
        related_name='education',
        blank=True,
    )
    experience = models.CharField(
        verbose_name='Стаж',
        max_length=1000,
        blank=True,
        null=True
    )
    cabinet = models.ManyToManyField(
        'Adress',
        verbose_name='Кабинет',
        related_name='adress',
        blank=True,
    )
    personal_consultation = models.CharField(
        verbose_name='Личная встреча',
        max_length=1000,
        blank=True,
        null=True
    )
    online_consultation = models.CharField(
        verbose_name='Онлайн-консультация',
        max_length=1000,
        blank=True,
        null=True
    )
    duration_consultation = models.CharField(
        verbose_name='Длительность консультации',
        max_length=1000,
        blank=True,
        null=True
    )
    couple_consultation_duration = models.CharField(
        verbose_name='Длительность консультации для пар',
        max_length=1000,
        blank=True,
        null=True
    )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        blank=True,
    )
    updated = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True,
        blank=True
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('view_employer', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''{self.name} -
        '''

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
        ordering = ['name']


class Adress(models.Model):
    cabinet = models.CharField(
        verbose_name='Кабинет',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_adress', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''{self.cabinet} -
        '''

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['cabinet']


class Education(models.Model):
    university = models.CharField(
        verbose_name='Университет',
        max_length=1000,
        blank=True,
        null=True
    )
    skill = models.CharField(
        verbose_name='Квалификация',
        max_length=1000,
        blank=True,
        null=True
    )
    education_date = models.DateTimeField(
        verbose_name='Год получения',
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_education', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''{self.university} -
        {self.skill} -
        {self.education_date} -
        '''

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'
        ordering = ['university']


class Category(models.Model):
    direction = models.CharField(
        'Направление',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_category', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''- {self.direction}
        '''

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['direction']


class Activity(models.Model):
    work = models.CharField(
        'Деятельность',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_activity', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''- {self.work}
        '''

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'
        ordering = ['work']


class Location(models.Model):
    city = models.CharField(
        'Город',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_location', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''г. {self.city} 
        '''

    class Meta:
        verbose_name = 'Местонахождение'
        verbose_name_plural = 'Местонахождения'
        ordering = ['city']


class Application(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'{self.employer}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-date']


class Slider(models.Model):
    image = models.ImageField(
        upload_to='slider/'
    )
    title = models.CharField(
        max_length=50
    )
    content = models.CharField(
        max_length=200,
        blank=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['-date']
