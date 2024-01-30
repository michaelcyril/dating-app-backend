from django.db import models
import uuid
from user_management.models import Account
from django.conf import settings

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


class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="convo_starter"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="convo_participant"
    )
    start_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "conversation"


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              null=True, related_name='message_sender')
    text = models.CharField(max_length=200, blank=True)
    # attachment = models.FileField(blank=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE,)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)
        db_table = "message"
