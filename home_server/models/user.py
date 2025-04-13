from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token as DefaultTokenModel
from django.contrib.auth.models import AbstractUser



class ClientUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255, unique=True,blank=True,null=True)
    limits = models.IntegerField(default=5) 
    address = models.TextField(blank=True,null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True,blank=True,null=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


    class Meta:
        db_table="home_server"


class ClientUserToken(DefaultTokenModel):
    user = models.OneToOneField(ClientUser, on_delete=models.CASCADE, related_name='auth_token')





class UserLimitHistory(models.Model):
    TRANSACTION_TYPES = [
        ('increase_limit', 'Increase  Limit'),
        ('decrease_limit', 'Decrease Limit'),
        ('other', 'Other'),
    ]

    account = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPES)
    new_limit  = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account.username} - {self.transaction_type} - {self.new_limit }"
