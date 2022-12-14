from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # defines how this object wil be displayed when returned on the admin page
    # instead of just returning the profile object 
    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:  #shrink image to 300px x 300 px
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

