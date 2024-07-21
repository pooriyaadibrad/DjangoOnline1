from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
from . import form
# Create your views here.
def landing(request):
    form1=form.LandingForm()
    return render(request, 'index.html',context={'form':form1})
def sendMessage(request):
    print('if whats work say me hello')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        PhoneNumber= request.POST.get('PhoneNumber')
        message = request.POST.get('message')
        instance=models.message.objects.create(name=name,email=email,PhoneNumber=PhoneNumber,message=message)
        instance.save()
        messages.success(request, 'کامنت شما موفقیت آمیز ثبت شد ')
        return redirect('landing')
    else:
        messages.success(request, 'اشکالی پیش امد ')
        return redirect('landing')