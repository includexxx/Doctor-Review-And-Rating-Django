from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
from doctor.models import DoctorProfile

class Rating(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(DoctorProfile, verbose_name='Doctor Profile',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:10]

