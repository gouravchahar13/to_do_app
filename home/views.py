from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import task as t

# Create your views here.
def home(request):
    queryset=t.objects.all()
    context={'tasks':queryset}
    return render(request,'index.html',context)

def submit(request):
    if request.method=='POST':
        task=request.POST.get('task')
        tasks=t.objects.create(
            task=task
        )
        messages.info(request,'task added')
        return redirect('home')
    else:
        return HttpResponse('SERVER ERROR')
    
def delete(request,id):
    t.objects.filter(id=id).delete()
    return redirect('home')