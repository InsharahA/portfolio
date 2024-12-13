from django.db import models
from django.conf import settings
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField()  # Link to more details
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the project

    def __str__(self):
        return self.title
