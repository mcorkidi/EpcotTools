from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'core/home.html')


def caja(request):
    
    if request.user.is_authenticated():

        return render(request, 'core/caja.html')
    else:

        return render(request, 'users/login.html')
