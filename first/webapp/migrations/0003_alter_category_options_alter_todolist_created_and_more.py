# Generated by Django 5.0 on 2024-02-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_category_todolist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
