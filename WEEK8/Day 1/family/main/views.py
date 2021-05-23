from django.shortcuts import render
from datetime import datetime
# Create your views here.

def site(request):

    today = datetime.now()
    return render(request, 'site.html', 
        {'now':today, 'myname':'Toby', 'letters':list('abcdefg')})

def about(request, myname):
    return render(request, 'about.html', {'name':myname})