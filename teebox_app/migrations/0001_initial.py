# Generated by Django 5.0.1 on 2024-01-25 22:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_app', '0002_course_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teebox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color1', models.CharField(max_length=10)),
                ('color2', models.CharField(blank=True, max_length=10, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
