# Generated by Django 4.0.5 on 2022-08-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tinder', '0012_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Участник', 'verbose_name_plural': 'Участники'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], max_length=1, verbose_name='Пол'),
        ),
    ]