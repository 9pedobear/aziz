# Generated by Django 4.0.3 on 2022-03-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0006_adress_remove_employer_cabinet_employer_cabinet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='surname',
        ),
        migrations.AlterField(
            model_name='employer',
            name='cabinet',
            field=models.ManyToManyField(blank=True, related_name='adress', to='employer.adress', verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='direction',
            field=models.ManyToManyField(blank=True, related_name='category', to='employer.category', verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='education',
            field=models.ManyToManyField(blank=True, related_name='education', to='employer.education', verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='ФИО'),
        ),
    ]