from django.shortcuts import render

# Create your views here.
def index_page_view(request):
    data = {
        "name" : "Varsha",
        "course" : "Python Backend Development Live"
    }
    return render(request, "index.html",context=data)