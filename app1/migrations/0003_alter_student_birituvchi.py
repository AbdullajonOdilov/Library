# Generated by Django 4.1 on 2022-09-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_tugatil_y_muallif_t_y_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birituvchi',
            field=models.BooleanField(default=False),
        ),
    ]