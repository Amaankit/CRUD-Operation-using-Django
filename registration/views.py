from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#Home Page
def addAndShow(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            reg=User(name=name,email=email,password=password)
            reg.save()
            fm=StudentRegistration() 
    else:
        fm=StudentRegistration()  
    st=User.objects.all()

    return render(request,'registration/addshow.html',{'form':fm,'stud':st})
#Delete Data
def deleteData(request,my_id):
    if request.method=='POST':
        pi=User.objects.get(pk=my_id)
        pi.delete()
        return HttpResponseRedirect('/')
def updateData(request,my_id):
    if request.method=='POST':
        pi=User.objects.get(pk=my_id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration() 
    else:
        pi=User.objects.get(pk=my_id)
        fm=StudentRegistration(instance=pi)




    return render(request,'registration/update.html',{'form':fm})

