# Generated by Django 2.2.16 on 2020-11-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
            ],
        ),
    ]
