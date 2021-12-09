from django.shortcuts import render

# Create your views here.
#request: get and post
def index(request):
    return render(request, 'MainApp/index.html')
    