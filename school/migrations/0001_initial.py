# Generated by Django 4.1.5 on 2023-01-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fathers_name', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(choices=[('PUR', 'PURNEA'), ('PAT', 'PATNA'), ('BHOPAL', 'BHOPAL'), ('RANCHI', 'RANCHI')], max_length=200)),
            ],
        ),
    ]
