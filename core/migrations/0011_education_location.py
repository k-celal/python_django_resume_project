# Generated by Django 4.1.5 on 2024-02-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.CharField(blank=True, default='', help_text='Location of the school', max_length=254, verbose_name='Location'),
        ),
    ]
