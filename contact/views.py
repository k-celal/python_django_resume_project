from django.http import JsonResponse
from django.shortcuts import render
from contact.models import Message
# Create your views here.
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Message.objects.create(name=name, email=email, subject=subject, message=message)
        success = True
        message = 'Message sent successfully'
    else:
        success = False
        message = 'Invalid request method'

    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)
def contact(request):
    return render(request, 'contact.html')