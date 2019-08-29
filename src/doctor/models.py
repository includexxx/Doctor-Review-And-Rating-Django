from django.db import models
import random, os
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save

User = get_user_model()


class Specialty(models.Model):
    title       = models.CharField(max_length = 255)
    created     = models.DateTimeField(auto_now=True)
    updated     = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title 



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "doctors/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )
Gender = (
    ('All', 'all'),
    ('Male', 'male'),
    ('Female', 'female')
)

class DoctorProfile(models.Model):
    user            = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name       = models.CharField(max_length=255)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    specialty       = models.ManyToManyField(Specialty, related_name='specialty', verbose_name='Specialty')
    gender          = models.CharField(choices=Gender, default='All', max_length=6)

    class Meta:
        verbose_name = 'Doctor'

    def __str__(self):
        return self.full_name


# def save_profile(sender, instance, **kwargs):
#     #instance.profile.save()
#     if instance.image is None:
#         instance.image = 'images/noimage.png'
#     instance.image.save()

# pre_save.connect(save_profile, sender=DoctorProfile)



