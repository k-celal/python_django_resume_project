# Generated by Django 4.1.5 on 2024-04-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Date when the record was last updated', verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date when the record was created', verbose_name='Created Date')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='Subject')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-created_date'],
            },
        ),
    ]
