from django.db import models

# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(default='',max_length=254,blank=True,verbose_name='Setting Name',help_text='Name of the setting')
    description = models.CharField(default='',max_length=254,blank=True,verbose_name='Description',help_text='Description of the setting')
    parameter = models.CharField(default='',max_length=254,blank=True,verbose_name='Parameter',help_text='Parameter name')
    updated_date = models.DateTimeField(auto_now=True,blank=True,verbose_name='Updated Date',help_text='Date when the record was last updated')
    created_date = models.DateTimeField(auto_now_add=True,blank=True,verbose_name='Created Date',help_text='Date when the record was created')
    def __str__(self):
        return f'General Setting: {self.name}'
    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering=('name','parameter')