# Generated by Django 4.0.4 on 2022-04-22 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('fechaDeNac', models.DateField()),
            ],
        ),
    ]
