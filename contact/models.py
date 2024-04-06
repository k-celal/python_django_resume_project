from django.db import models
from core.models import AbstractBase
# Create your models here.
class Message(AbstractBase):
    name = models.CharField(max_length=255, blank=True, verbose_name='Name')
    email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
    subject = models.CharField(max_length=255, blank=True, verbose_name='Subject')
    message = models.TextField(blank=True, verbose_name='Message')

    def __str__(self):
        return f'Message: {self.name}'
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created_date']