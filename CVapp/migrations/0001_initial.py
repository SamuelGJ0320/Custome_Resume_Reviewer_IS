# Generated by Django 5.1.1 on 2024-10-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImprovedCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_cv', models.TextField()),
                ('vacancy_description', models.TextField()),
                ('improved_cv', models.TextField()),
            ],
        ),
    ]
