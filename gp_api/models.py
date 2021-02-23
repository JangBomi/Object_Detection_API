from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Notes(models.Model):
    text = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, related_name="notes", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.text
