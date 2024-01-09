from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import movies


# Create your views here.
def index(request):
    movie=movies.objects.all()
    return render(request,'index.html',{'movie_list':movie})
def detail(request,movies_id):
    movie=movies.objects.get(id=movies_id)
    return render(request,'detail.html',{'movie':movie})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        image = request.FILES['image']
        movie=movies(name=name,desc=desc,year=year,image=image)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=movies.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')