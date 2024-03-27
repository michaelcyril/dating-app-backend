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
    GENDER_STATUS =(
        ("MALE","user is male"),
        ("FEMALE","user is female"),
        ("NONE","user is female"),
        
        
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    gender = models.CharField(choices=GENDER_STATUS,default='NONE',max_length=20, null=True)
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


class Tag(models.Model):
    name =  models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# Create your models here.
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=250, null=True, blank=True)
    work = models.CharField(max_length=250, null=True, blank=True)
    profile = models.ImageField(upload_to="uploads/", null=True, blank=True)
    dob = models.DateTimeField(null=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag,blank=True)
    lat = models.CharField(max_length=250, null=True, blank=True)
    long = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'account'


# class TrashBin(models.Model):
#     id = models.CharField(max_length=255, primary_key=True)
#     location = models.CharField(max_length=255)
#     work = models.CharField(max_length=255)
#     lat = models.FloatField()
#     long = models.FloatField()
#     bio = models.CharField(max_length=255)

#     def __str__(self):
#         return self.id
    
#     class Meta:
#         db_table = 'trash'
        