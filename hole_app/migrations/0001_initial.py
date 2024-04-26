# Generated by Django 5.0.1 on 2024-01-30 21:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teebox_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('par', models.PositiveSmallIntegerField()),
                ('distance', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=10)),
                ('teebox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teebox_app.teebox')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
