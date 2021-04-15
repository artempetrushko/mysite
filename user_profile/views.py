from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from notebook.forms import NoteForm
from notebook.models import Note
from .serializers import UserSerializer
from rest_framework import generics


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) != 0:
        notes = Note.objects.all()
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.save()
        return render(request, 'index.html', {'user': user[0], 'notes': notes, 'form': form, 'isIndexPage': True})
    else:
        return redirect('login')


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'user': user, 'isIndexPage': False})
        else:
            return render(request, 'login.html', {'invalid': True})
    else:
        return render(request, 'login.html', {'invalid': False})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    form = RegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = request.POST["username"]
            existing_user = User.objects.filter(username=username)
            if len(existing_user) == 0:
                password = request.POST["password"]
                user = User.objects.create_user(username, '', password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return render(request, 'index.html', {'user': user})
            else:
                return render(request, 'registration.html', {'form': form, 'invalid': True})
        else:
            return render(request, 'registration.html', {'form': form, 'invalid': True})
    else:
        return render(request, 'registration.html', {'form': form, 'invalid': False})


