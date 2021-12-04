from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Cuenta {username} creada!')
            return redirect('home-blog')
    else:
        form = UserRegisterForm()
    return render(request, 'user/registro.html', {'form': form})
    