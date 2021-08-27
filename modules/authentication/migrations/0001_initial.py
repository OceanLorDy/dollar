# Generated by Django 3.2.6 on 2021-08-24 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Last Name')),
                ('username', models.CharField(max_length=99, verbose_name='Username')),
                ('password', models.CharField(max_length=99, verbose_name='Password')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]