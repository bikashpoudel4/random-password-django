from django.shortcuts import render

#MANUALLY________________________
from django.http import HttpResponse
import random
#MANUALLY___________ENDS_________

#MANUALLY___________

def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # Freom html <input type="checkbox" name="uppercase"> Uppercase
    # extend is used for adding letters or extending List of above characters
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    # path('FUNCTION/', views.FUNCTION)
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    # here {'password':thepassword } is dictionary that we wanna render in template
    return render(request, 'passwordT.html', {'password':thepassword})

def about(requset):
    return render(requset, 'about.html')
#MANUALLY___________ENDS_________
