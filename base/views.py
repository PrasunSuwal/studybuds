from django.shortcuts import render, redirect
from .models import *
from .forms import RoomForm

# Create your views here.

def index(request):
    rooms = Room.objects.all()
    return render(request, 'base/index.html', {'rooms':rooms})

def user_login(request):
    return render(request, 'base/login.html')

def user_signup(request):
    return render(request, 'base/register.html')

def room(request):
    return render(request, 'base/room.html ')

def room_form(request):    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = RoomForm()
    return render(request, 'base/room_form.html', {'form':form})



def delete(request):
    return render(request, 'base/delete.html ')

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'base/room_form.html', {'form':form})


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('index')
    return render(request, 'base/delete.html',{'obj':room})