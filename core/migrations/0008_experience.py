# Generated by Django 4.1.5 on 2024-02-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_skill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Date when the record was last updated', verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date when the record was created', verbose_name='Created Date')),
                ('company', models.CharField(blank=True, default='', help_text='Name of the company', max_length=254, verbose_name='Company')),
                ('job_title', models.CharField(blank=True, default='', help_text='Job title in the company', max_length=254, verbose_name='Job Title')),
                ('position', models.CharField(blank=True, default='', help_text='Position in the company', max_length=254, verbose_name='Position')),
                ('start_date', models.DateField(blank=True, help_text='Start date of the experience', verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, help_text='End date of the experience', null=True, verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'ordering': ('start_date',),
            },
        ),
    ]
