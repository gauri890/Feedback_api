from django.shortcuts import render
from .forms import feedbackform

# Create your views here.

def home(request):
    context={}

    form = feedbackform(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request,'home.html',context)

