# Generated by Django 3.1.3 on 2020-11-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_option_about_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='icon',
            field=models.CharField(max_length=50),
        ),
    ]
