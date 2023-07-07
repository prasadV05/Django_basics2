from django.shortcuts import render
from my_app.models import My_app
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index_view(request):
    return HttpResponse("<h1>Hello World</h1>")

def my_app_detail_views(request, my_app_id):
    try:
        my_app_object= My_app.objects.get(pk=my_app_id)
    except My_app.DoesNotExist:
        return JsonResponse({"error" : True, "message" : "My_app does not exist"})
    return JsonResponse({
        "id" : my_app_object.id,
        "name" : my_app_object.name,
        "age" : my_app_object.age
    })