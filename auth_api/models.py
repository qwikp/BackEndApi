from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class SMSLog(models.Model):
    uid = models.UUIDField(verbose_name=_('UUID'), unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        to=get_user_model(), verbose_name=_('user'), null=True, blank=True, on_delete=models.CASCADE,
        related_name='sms_logs'
    )
    phone_no = models.CharField(max_length=20)
    message = models.TextField(verbose_name=_('message'), max_length=500, null=True, blank=True)
    transaction_id = models.CharField(verbose_name=_('transaction ID'), max_length=100)
    server_message_id = models.CharField(verbose_name=_('server message id'), max_length=100, null=True, blank=True)
    server_response = models.TextField(verbose_name=_('server response'), null=True, blank=True)
    last_status = models.CharField(verbose_name=_('last status'), max_length=30)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), null=True, blank=True)
