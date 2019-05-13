from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def search_category(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = (request.GET.get("category")).title()
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-gallery/search.html',{"message":message})    
