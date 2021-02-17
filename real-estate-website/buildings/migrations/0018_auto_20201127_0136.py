# Generated by Django 3.1.3 on 2020-11-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0017_auto_20201127_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='has_parking',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='estate',
            name='transportation',
            field=models.CharField(choices=[('far', 'Far'), ('close', 'Close')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='estate',
            name='utility_included',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3, null=True),
        ),
    ]
