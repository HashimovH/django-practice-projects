# Generated by Django 3.0.4 on 2020-03-30 11:30

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('about', models.CharField(max_length=150)),
                ('facebook', models.URLField()),
                ('linkedin', models.URLField()),
                ('goodwall', models.URLField()),
                ('twitter', models.URLField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
