from django.shortcuts import render, redirect
from .forms import (
    RegistrationForm,
    LoginForm,
    EditProfileForm,
    NotePadForm,
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,
)
from .models import resort_room, notepad
from django.db.models import Q
from django.contrib import messages

# Create your views here.
#-------- Home -----------
def home(request):
    return render(request, 'resort/home.html')

#-------- Registration -----------
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Registration complete successfully')
            return redirect('/athletic_resort/login')
        else:
            messages.error(request, 'Please enter correct information')
            return redirect('/athletic_resort/registration')
    else:
        form = RegistrationForm()
        arg = {'form': form}
    return render(request, 'resort/registration.html', arg)

#-------- Log in -----------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not user:
                messages.error(request, 'Username and Password did not matched')
                return redirect('/athletic_resort/login')
            login(request, user)
            return redirect('/athletic_resort/home')
    else:
        form = LoginForm()
        arg = {'form': form}
    return render(request, 'resort/login.html', arg)

#-------- Log out -----------
def logout_view(request):
    logout(request)
    return redirect('/athletic_resort/login')

#-------- Profile -----------
def profile(request):
    return render(request, 'resort/profile.html')

#-------- Edit Profile -----------
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update successfully')
            return redirect('/athletic_resort/profile')
    else:
        form = EditProfileForm(instance=request.user)
        arg = {'form': form}
    return render(request, 'resort/edit_profile.html', arg)

#-------- Change Password -----------
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('/athletic_resort/profile')
        else:
            messages.error(request, 'Did not match')
            return redirect('/athletic_resort/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        arg = {'form': form}
    return render(request, 'resort/change_password.html', arg)

#-------- Room_List -----------
def room_list(request):
    room = resort_room.objects.all()

    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = resort_room.objects.filter(Q(room_type__icontains=search))
            if match:
                return render(request, 'resort/room_list.html', {'sr': match})
            else:
                messages.error(request, 'No result found')
        else:
            return redirect('/athletic_resort/room_list')
    arg = {'room': room}
    return render(request, 'resort/room_list.html', arg)

#-------- Room_Details -----------
def room_details(request, id, room_type):
    room_detail = resort_room.objects.filter(id=id, room_type=room_type)
    arg = {'rooms': room_detail}
    return render(request, 'resort/room_details.html', arg)

#-------- Note Pad -----------
def note_pad(request):
    note_pad_all = notepad.objects.all()
    if request.method == 'POST':
        form = NotePadForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
            return redirect('/athletic_resort/note_pad')
    else:
        form = NotePadForm()
        arg = {
            'form': form,
            'note_pad_all': note_pad_all
            }
    return render(request, 'resort/note_pad.html', arg)