from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # defines how this object wil be displayed when returned on the admin page
    # instead of just returning the profile object 
    def __str__(self) -> str:
        return f'{self.user.username} Profile'