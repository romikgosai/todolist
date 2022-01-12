# Generated by Django 4.1.dev20211217120704 on 2022-01-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('completed', models.BooleanField(default=False)),
                ('important', models.BooleanField(default=False)),
            ],
        ),
    ]
