from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    mf_year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
