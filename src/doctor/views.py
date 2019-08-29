from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import DoctorProfile, Specialty
from rating.forms import RatingForm
from rating.models import Rating


class DoctorList(ListView):
    model               = DoctorProfile
    context_object_name = "doctors"
    template_name       = 'doctor/doctor_list.html'
    paginate_by         = 3

    def get_queryset(self):
        speciality = self.request.GET.get('specility')
        name       = self.request.GET.get('name')
        gender     = self.request.GET.get('gender')
        qs         = DoctorProfile.objects.all()
        if gender and gender is not 'all':
            qs = qs.filter(gender__iexact = gender)
        if speciality:
            qs = qs.filter(specialty__in=[speciality] )
        if name:
            qs = qs.filter(full_name__icontains=name )
        # import pdb 
        # pdb.set_trace()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(DoctorList, self). get_context_data( *args, **kwargs)
        context ['specilities'] = Specialty.objects.all()
        return context
    
    class Meta:
        ordering = ['id']



class DoctorDetail(DetailView):
    model               = DoctorProfile
    context_object_name = "doctor"
    template_name       = 'doctor/doctor_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DoctorDetail, self). get_context_data( *args, **kwargs)
        context['form'] = RatingForm()
        context['form'].fields['profile_id'].initial = kwargs['object'].id
        context['ratings'] = Rating.objects.all()
        return context
    