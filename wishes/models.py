from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Wishes(models.Model):

    class Status(models.TextChoices):
        OPEN = "Open"
        PENDING = "Pending"
        FULFILLED = "Fulfilled"

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.OPEN)
    main_photo = models.ImageField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField(blank=True)
    list_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Wishes"
