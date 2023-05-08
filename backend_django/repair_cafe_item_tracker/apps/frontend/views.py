from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "frontend/index.html")

def add_item(request):
    return render(request, "frontend/add_item.html")
