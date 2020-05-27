from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MemberForm
from django.core.mail import send_mail
from .models import ComMember
# Create your views here.

def index(request):
    print(request.POST)
    
    form = MemberForm(request.POST)
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['to@example.com'],

    #     fail_silently=False,
    # )
    if request.method == 'POST':    
        if form.is_valid():
            form.save()
    context = {'form': form}
            
    return render(request, 'base/index.html',context)

