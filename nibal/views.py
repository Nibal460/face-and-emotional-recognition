from django.shortcuts import render
from django.http import HttpResponse
from nibal.forms import faceform
from nibal.machinelearning import pipeline_model
from django.conf import settings
from nibal.models import face
import os
# Create your views here.


def index(request):
    form = faceform()
    
    if request.method =='POST':
        form = faceform(request.POST or None, request.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)
          
          
        
           # extract the image objectform database
            primary_key = save.pk
            imgobj = face.objects.get(pk=primary_key)
            fileroot = str(imgobj.image)
            filepath = os.path.join(settings.MEDIA_ROOT,fileroot)
            results = pipeline_model(filepath)
            print(results)
           
           
            return render(request,'index.html',{'form':form,'upload':True,'results':results})
           
           
    return render(request,'index.html',{'form':form,'upload':False})
                  


           
 
       

