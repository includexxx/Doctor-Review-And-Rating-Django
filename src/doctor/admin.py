from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import DoctorProfile


class DoctorAdmin(admin.ModelAdmin):

    list_display = ('id','user','full_name', 'image', 'gender')


admin.site.register(DoctorProfile, DoctorAdmin)


