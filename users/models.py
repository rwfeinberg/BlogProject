from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Profile Model used in User app
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)             # Defines 1-to-1 existence of user and profile

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # Defines profile picture location and default

    def __str__(self):
        return f'{self.user.username} Profile'                  # Overriden function to return when profile is called

    # def save(self, *args, **kwargs):                                             # Overriden function to correctly update and resize profile pic
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

