from django.shortcuts import render

from django.shortcuts import render
# Create your views here.
from .models import Objects

def index(request):
    if request.method == 'POST':
        if(request.POST.get('title')):
            post = Objects()
            post.data = request.POST.get('title')
            post.save()

    return render(request,'index.html')
