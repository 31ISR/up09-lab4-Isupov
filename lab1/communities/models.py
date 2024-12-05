from django.db import models

class Communities(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title