from django.shortcuts import HttpResponse, render

# CBV - Class Based View
# FBV - Function Based View

def hello_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    

def test_view(request):
    if request.method == 'GET':
        return HttpResponse('TEST VIEW')
