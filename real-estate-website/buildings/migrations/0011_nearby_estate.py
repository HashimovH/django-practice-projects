# Generated by Django 3.1.3 on 2020-11-18 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0010_estate_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearby',
            name='estate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildings.estate'),
        ),
    ]