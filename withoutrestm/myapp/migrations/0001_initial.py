# Generated by Django 4.1.3 on 2022-12-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=40)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
