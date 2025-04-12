# from msilib.schema import ListView

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'cafe/index.html')
#
# class CafeListView(ListView):
#     template_name = 'cafe/cafe_list.html'
#     context_object_name = 'cafes'

def menu(request):
    return render(request, 'cafe/menu.html')