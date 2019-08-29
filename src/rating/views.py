from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RatingForm
from doctor.models import DoctorProfile
from rating.models import Rating

def rating_create(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            id_of_profile = form.cleaned_data['profile_id']
            doctor = DoctorProfile.objects.get(id=id_of_profile)
            rating_obj = Rating()
            if not request.user.is_doctor:
                rating_obj.user = request.user
                rating_obj.profile = doctor
                rating_obj.comment = form.cleaned_data['comment']
                rating_obj.rating = form.cleaned_data['rating']
                rating_obj.save()
                
        return redirect(reverse_lazy('doctor:doctor_detail',kwargs={ 'pk': id_of_profile } ))
            
    else:
        form = RatingForm()
    return render(request, "doctor/doctor_detail.html", {"form" : form })
