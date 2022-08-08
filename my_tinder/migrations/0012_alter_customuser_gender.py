# Generated by Django 4.0.5 on 2022-08-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tinder', '0011_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], default='Male', max_length=6, verbose_name='Gender'),
        ),
    ]
