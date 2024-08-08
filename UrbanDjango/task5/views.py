from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Форма с джанго

users = ['user1', 'user2', 'user3']

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in users:
                return render(request, 'fifth_task/registration_done.html', {'username': username})
            else:
                info = {'error': 'User already exists'}
                if password != repeat_password:
                    info['error'] = 'Passwords do not match'
                if age < 18:
                    info['error'] = 'You must be over 18'
                return render(request, 'fifth_task/registration.html', {'form': form, 'info': info})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration.html', {'form': form})




# форма html
def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and age >= 18 and username not in users:
            return render(request, 'fifth_task/registration_done.html', {'username': username})
        else:
            info = {'error': 'User already exists'}
            if password != repeat_password:
                info['error'] = 'Passwords do not match'
            if age < 18:
                info['error'] = 'You must be over 18'
            return render(request, 'fifth_task/registration.html', {'info': info})
    else:
        return render(request, 'fifth_task/registration.html')



