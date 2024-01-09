from django.shortcuts import render
from shop.models import product
from django.db.models import Q




def searchresult(request):
    Product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        Product=product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
        return render(request,'search.html',{'query':query,'products':Product})

