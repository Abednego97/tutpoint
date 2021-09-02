from django.shortcuts import render,redirect
from.models import register
from django.contrib import messages


# Create your views here.
def index(request):
    
    return render(request,"regist/index.html")

def contact(request):
    return render(request, "regist/contact.html")

def registere(request):
    todo = register.objects.all()
    if request.method == 'POST':
        regist = register(
            email = request.POST['email'],
            name =request.POST['name'],
            whatsapp = request.POST['whatsapp'],
            number = request.POST['number'],
            learn = request.POST['learn']
        )
        regist.save()
        messages.success(request,"Registration Successful")
        return redirect('index')
    return render(request=request,template_name='regist/register.html',context={'todos':todo})
