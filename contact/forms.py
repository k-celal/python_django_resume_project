from django import forms
from django.conf import settings
from django.core.mail import EmailMessage
class ContactForm(forms.Form):
    name = forms.CharField(max_length=254,required=True)
    email = forms.EmailField(max_length=254,required=True)
    subject = forms.CharField(max_length=254,required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)

    def send_mail(self):
        if self.is_valid():
            name = self.cleaned_data.get('name')
            email = self.cleaned_data.get('email')
            subject = self.cleaned_data.get('subject')
            message = self.cleaned_data.get('message')
            message_context = 'Meesage Received.\n\n' \
                              'Name: %s\n' \
                              'Email: %s\n' \
                              'Subject: %s\n' \
                              'Message: %s' % (name, email, subject, message)
            email = EmailMessage(
                subject=subject,
                body=message_context,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],)
            email.send()