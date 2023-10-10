from django.shortcuts import render
from .forms import WorkerRegistration,SearchWorkers
from .models import WorkerDetails
def RegisterWorker(request):
    form=WorkerRegistration()
    if request.method=='POST':
        form=WorkerRegistration(request.POST)
        if(form.is_valid()):
            worker=WorkerDetails(First_Name=form.cleaned_data['First_Name'],Middle_Name=form.cleaned_data['Middle_Name'],Last_Name=form.cleaned_data['Last_Name'],Mobile_Number=form.cleaned_data['Mobile_Number'],Gender=form.cleaned_data['Gender'],Age=form.cleaned_data['Age'],Address=form.cleaned_data['Address'],Pin_Code=form.cleaned_data['Pin'])
            worker.save()  
    else:
        form=WorkerRegistration()
    return render(request,'KnowWorker/WorkerRegistration.html',{'form':form})

def searchWorker(request):
    form=SearchWorkers()
    error=''
    if(request.method=='POST'):
        form=SearchWorkers(request.POST)
        if(form.is_valid()):
         pincode=form.cleaned_data['Area_Pin']
         workersData=WorkerDetails.objects.filter(Pin_Code=pincode)
         if(workersData):
          return render(request,'KnowWorker/SearchWorker.html',{'form':form,'workersData':workersData})
         else:
            form=SearchWorkers()
            error='Enter Valid Area Pin'
       
            
    return render(request,'KnowWorker/SearchWorker.html',{'form':form,'error':error})
             
def knowWorkerSubmodule(request):
   return render(request,'knowWorker/knowWorkerSubmodule.html')
# Create your views here.
