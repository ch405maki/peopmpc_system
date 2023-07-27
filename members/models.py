from django.db import models

class Member(models.Model):
    # Your existing fields
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    profile_picture = models.ImageField(default='profile.png', upload_to='profile_pics')

    def __str__(self):
        return self.name
