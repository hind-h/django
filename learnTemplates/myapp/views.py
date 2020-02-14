from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def relative(request):
    return render(request, 'myapp/relative_urltemplates.html')

def other(request):
    dct = {'text':'Hello world'}
    return render(request, 'myapp/other.html', dct)
