from django.db import models
from django.contrib.auth.models import AbstractUser

class Worker(AbstractUser):
    worker_name = models.CharField(max_length=40, verbose_name='Enter your name')
    email_id = models.EmailField(max_length=80, unique=True)
    phone_number = models.CharField(max_length=20, default='', null=True)
    address = models.CharField(max_length=255, default='', blank=True)
    skills = models.CharField(max_length=255)
    experience = models.IntegerField(default=0)  # Number of years of experience
    is_approved = models.BooleanField(default=False)  # Approval by admin

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='worker_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='worker_user_permissions',
        blank=True
    )

    def __str__(self):
        return self.worker_name
    
