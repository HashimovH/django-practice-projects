# Generated by Django 3.1.3 on 2020-11-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0012_auto_20201118_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]