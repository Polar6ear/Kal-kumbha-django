from .models import Category
def menu_links(request):
    links = Category.objects.filter()
    return dict(links=links)