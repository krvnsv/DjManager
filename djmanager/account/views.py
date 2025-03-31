from django.shortcuts import redirect, render

from .models import User

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)

            print('User created: ', user)

            return redirect('/login/')
        else:
            print('Something went wrong')
    else:
        print('Just show the form')

    return render(request, 'account/signup.html')