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


class User(models.Model):
    name = models.CharField(max_length=255)
    userId = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)
    birthDate = models.DateField('yyyymmdd')

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=255)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField
    recordNum = models.IntegerField()
    etc = models.CharField(max_length=255)
    userId = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class RecordDetail(models.Model):
    detectedItem = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    captureTime = models.DateTimeField()
    recordId = models.ForeignKey(
        Record, related_name="record", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.detectedItem