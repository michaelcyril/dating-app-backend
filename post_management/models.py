from django.db import models
from user_management.models import Account
import uuid

# Create your models here.
class Image(models.Model):
    STATUS = (
        ("DELETED", "Deleted post"),
        ("ACTIVE", "Active post"),
        ("INACTIVE", "Inactive post"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/post_images/", null=True, blank=True)
    status = models.CharField(choices=STATUS, default='INACTIVE', max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'image'

class Video(models.Model):
    STATUS = (
        ("DELETED", "Deleted post"),
        ("ACTIVE", "Active post"),
        ("INACTIVE", "Inactive post"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    video = models.FileField(upload_to="uploads/post_video/", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="uploads/post_video/thumbnails/", null=True, blank=True)
    status = models.CharField(choices=STATUS, default='INACTIVE', max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'video'


