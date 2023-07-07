from django.shortcuts import render

# Create your views here.
def index_page_view(request):
    data = {
        "show_data" : True,
        "name" : "Varsha",
        "course" : "Python Backend Development Live",
        "list" : [1,2,3,4]
    }
    return render(request, "index.html",context=data)