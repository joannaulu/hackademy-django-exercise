from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#    first_name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_images')
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    # def first_name(self):
    #   return self.user.first_name

    # def last_name(self):
    #   return self.user.last_name

    # def _str_(self):
    #   return.self.user.username