from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post-image/', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    # participants =
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
