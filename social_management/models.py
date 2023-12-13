from django.db import models
import uuid
from user_management.models import Account

# Create your models here.
class Like(models.Model):
    STATUS = (
        ("ACTIVE", "Active like"),
        ("INACTIVE", "Inactive like"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account,related_name="liked_account", on_delete=models.CASCADE)
    likedBy = models.ForeignKey(Account, related_name="liked_by",on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='INACTIVE', max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'like'



# class Chat(models.Model):
#     pass
