# Generated by Django 3.2.5 on 2021-09-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_auto_20210829_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
    ]
