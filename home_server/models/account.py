from django.db import models
from .user import ClientUser
import uuid


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ManageAccount(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, unique=True,blank=True,null=True)
    pass_key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # Unique UUID
    is_on_hold = models.BooleanField(default=False)  # Hold status
    delete_account = models.BooleanField(default=False)
    otp = models.CharField(max_length=10, blank=True, null=True)
    

    def __str__(self):
        return f"{self.phone} ({'On Hold' if self.is_on_hold else 'Active'})"

    class Meta:
        db_table = "ManageAccount"
  


class RequestLog(BaseModel):
    REQUEST_TYPES = [('increase_limit', 'Increase Limit'), ('user_hold', 'User Hold')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES, default='increase_limit')
    note = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    def __str__(self):
        return f"{self.client_user} - {self.request_type} at {self.created_at}"
    
    class Meta:
        db_table = "RequestLog"
    
