# Generated by Django 4.1.5 on 2024-02-29 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.CharField(blank=True, default='', help_text='Location of the company', max_length=254, verbose_name='Location'),
        ),
    ]
