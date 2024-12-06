from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'wodder/index.html')

def test_view(request):
    return render(request, 'wodder/test_view.html')

def user_page(request): # here the user can also submit workouts
    pass

