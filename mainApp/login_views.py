from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "¡Bienvenido de nuevo!")
            return redirect('home')
        
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})

def registro_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('home')
        else:
            messages.error(request, "Error al registrarse. Revisa los campos.")

    return render(request, 'login/registro.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada exitosamente.")
    return redirect('home')