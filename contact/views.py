from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from django.contrib import messages
from contact.models import Contact_us
# Create your views here.


def contactUs(request):
    if request.method=='POST':
        sender_name= request.POST.get('sender_name')
        from_email= request.POST.get('from_email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')
        admin='warriors.mart.contact@gmail.com'
        
        if subject and message and from_email:
           contact=Contact_us(sender_name=sender_name,from_email=from_email,subject=subject,message=message)
           contact.save()
           send_mail(subject,message,from_email, [admin,from_email,sender_name])
           messages.success(request,'Succesfully Send Message!')
        
         
        else:
           messages.error('Make sure all fields are entered and valid!')

    return render(request, 'contact.html')
