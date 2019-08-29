from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

from .forms import SignupForm
from doctor.forms import DoctorProfileForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(False)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            #check password is validate or not
            try:
                validate_password(raw_password, user)
            except ValidationError as e:
                form.add_error('password', e)  # to be displayed with the field's errors
                return render(request,'account/signup.html', {'form': form})

            user.set_password(raw_password)
            user.save()
            user = authenticate(username=user.email, password=raw_password)
            
            login(request, user)
            return redirect(reverse_lazy('doctor:home'))
            
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {"form": form})


def doctor_signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        doctor_profile_form  = DoctorProfileForm(request.POST, request.FILES)
        if form.is_valid() and doctor_profile_form.is_valid():
            user = form.save(False)
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            #check password is validate or not
            try:
                validate_password(raw_password, user)
            except ValidationError as e:
                form.add_error('password', e)  # to be displayed with the field's errors
                return render(request,'account/signup.html', {'form': form})

            user.set_password(raw_password)
            user.doctor = True
            user.save()
            user = authenticate(username=user.email, password=raw_password)
            login(request, user)
            #doctor profile save
            doctor = doctor_profile_form.save(commit=False)
            doctor.user = user 
            # import pdb 
            # pdb.set_trace()
            doctor.save()
            return redirect(reverse_lazy('doctor:home'))
            
    else:
        form = SignupForm()
        doctor_profile_form  = DoctorProfileForm()
    return render(request, 'account/doctor_signup.html', {"form": form, 'doctor_profile_form': doctor_profile_form})