from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    STATUS = (
        ("DELETED", "User deleted"),
        ("ACTIVE", "Active user"),
        ("INACTIVE", "Inactive user"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS, default='INACTIVE', max_length=20)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


# Create your models here.
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=250)
    work = models.CharField(max_length=250, null=True)
    profile = models.ImageField(upload_to="uploads/", null=True, blank=True)
    dob = models.DateTimeField()
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'account'

