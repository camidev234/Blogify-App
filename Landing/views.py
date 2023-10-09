from django.shortcuts import render

# Create your views here.


def indexLanding(request):
    return render(request, 'index.html')