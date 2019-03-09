from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from . import forms

import requests,json

COMPILE_URL = "https://api.hackerearth.com/v3/code/compile/"
RUN_URL = "https://api.hackerearth.com/v3/code/run/"

CLIENT_SECRET='6d2f6c5a5d56073090f845fff3058703a61202cc'



def runCode(request):
    
    if request.method=='POST':
        form=forms.code(request.POST)
        form=form.save(commit=False)
        source = form.code_input
        lang = form.lang
        data={
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': lang,
        'time_limit': 5,
        'memory_limit': 262144,
        }
        r=requests.post(RUN_URL,data=data)
        data=r.json()
        print(data)
        return render(request,'outcome.html',context={'my_dir':data})
        
    else:
        form=forms.code()
        context={'form':form}
        return render(request,'index.html',context) 









