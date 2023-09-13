from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import readforms

def index(request):
    events=Event.objects.all()
    context={
        'events':events
    }
    return render(request,'index.html',context)

def eventdetail(request,pk):
    event_single = Event.objects.get(pk=pk)
    if request.method == "POST":
        form=readforms(request.POST)
        if form.is_valid():
            read = form.save(commit=False)
            read.event = event_single
            read.save()
        print("I got a post request")
    form=readforms()
    context={
        'event':event_single,
        'form':form
    }
    return render(request,'details.html',context)
