from django.shortcuts import render,redirect
from main.models import show
from .forms import ShowForm

# Create your views here.

def display(request):
    form=show.objects.all()
    context={'form':form}
    return render(request, 'main/home.html',context)

def create_form(request):
    form=ShowForm()
    if request.method=="POST":
        form=ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display")
    context={'form':form}
    return render(request,"main/form_create.html", context)


def updateForm(request, pk):
    shows=show.objects.get(id=pk)
    form=ShowForm(instance=shows)
    if request.method=="POST":
        form=ShowForm(request.POST, instance=shows)
        if form.is_valid():
            form.save()
        return redirect('display')
    context={'form':form}
    return render(request,'main/form_create.html',context)


def deleteForm(request, pk):
    obj=show.objects.get(id=pk)
    obj.delete()
    return redirect('display')

