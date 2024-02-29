from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class AbstractBase(models.Model):
    updated_date = models.DateTimeField(auto_now=True,blank=True,verbose_name='Updated Date',help_text='Date when the record was last updated')
    created_date = models.DateTimeField(auto_now_add=True,blank=True,verbose_name='Created Date',help_text='Date when the record was created')
    class Meta:
        abstract = True
class GeneralSetting(AbstractBase) :
    name = models.CharField(default='',max_length=254,blank=True,verbose_name='Setting Name',help_text='Name of the setting')
    description = models.CharField(default='',max_length=254,blank=True,verbose_name='Description',help_text='Description of the setting')
    parameter = models.CharField(default='',max_length=254,blank=True,verbose_name='Parameter',help_text='Parameter name')
    def __str__(self):
        return f'General Setting: {self.name}'
    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering=('name','parameter')

class ImageSetting(AbstractBase):
    name = models.CharField(default='',max_length=254,blank=True,verbose_name='Setting Name',help_text='Name of the setting')
    description = models.CharField(default='',max_length=254,blank=True,verbose_name='Description',help_text='Description of the setting')
    image = models.ImageField(upload_to='images/',blank=True,verbose_name='Image',help_text='Image of the setting')
    def __str__(self):
        return f'Image Setting: {self.name}'
    class Meta:
        verbose_name = "Image Setting"
        verbose_name_plural = "Image Settings"
        ordering=('name','description')

class Skill(AbstractBase):
    order = models.PositiveIntegerField(default=0,verbose_name='Order',help_text='Order of the skill')
    name = models.CharField(default='',max_length=254,blank=True,verbose_name='Skill Name',help_text='Name of the skill')
    percentage = models.PositiveIntegerField(default=50,verbose_name='Percentage',validators=[MinValueValidator(0),MaxValueValidator(100)],help_text='Percentage of the skill')
    def __str__(self):
        return f'Skill: {self.name}'
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering=('order',)
class Experience(AbstractBase):
    company = models.CharField(default='',max_length=254,blank=True,verbose_name='Company',help_text='Name of the company')
    job_title = models.CharField(default='',max_length=254,blank=True,verbose_name='Job Title',help_text='Job title in the company')
    position = models.CharField(default='',max_length=254,blank=True,verbose_name='Position',help_text='Position in the company')
    location = models.CharField(default='',max_length=254,blank=True,verbose_name='Location',help_text='Location of the company')
    start_date = models.DateField(blank=True,verbose_name='Start Date',help_text='Start date of the experience')
    end_date = models.DateField(blank=True,null=True,verbose_name='End Date',help_text='End date of the experience')
    def __str__(self):
        return f'Experience: {self.company}'
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering=('start_date',) #- for descending order

class Education(AbstractBase):
    school_name = models.CharField(default='',max_length=254,blank=True,verbose_name='School Name',help_text='Name of the school')
    major = models.CharField(default='',max_length=254,blank=True,verbose_name='Major',help_text='Major in the school')
    department = models.CharField(default='',max_length=254,blank=True,verbose_name='Department',help_text='Department in the school')
    location = models.CharField(default='',max_length=254,blank=True,verbose_name='Location',help_text='Location of the school')
    start_date = models.DateField(blank=True,verbose_name='Start Date',help_text='Start date of the education')
    end_date = models.DateField(blank=True,null=True,verbose_name='End Date',help_text='End date of the education')
    def __str__(self):
        return f'Education: {self.school_name}'
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"
        ordering=('start_date',) #- for descending order

class SocialLink(AbstractBase):
    order = models.PositiveIntegerField(default=0,verbose_name='Order',help_text='Order of the social link')
    name = models.CharField(default='',max_length=254,blank=True,verbose_name='Name',help_text='Name of the social link')
    link = models.URLField(default='',max_length=254,blank=True,verbose_name='Link',help_text='Link of the social link')
    icon = models.CharField(default='',max_length=254,blank=True,verbose_name='Icon',help_text='Icon of the social link')
    def __str__(self):
        return f'Social Link: {self.link}'
    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
        ordering=('order',)