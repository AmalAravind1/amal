from .models import category

def menu_link(request):
    links=category.objects.all()
    return dict(link=links)