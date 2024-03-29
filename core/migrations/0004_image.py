# Generated by Django 4.1.5 on 2024-02-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_generalsetting_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='Name of the image', max_length=254, verbose_name='Image Name')),
                ('description', models.CharField(blank=True, default='', help_text='Description of the image', max_length=254, verbose_name='Description')),
                ('image', models.ImageField(help_text='Image file', upload_to='images/', verbose_name='Image')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Date when the record was last updated', verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date when the record was created', verbose_name='Created Date')),
            ],
        ),
    ]
