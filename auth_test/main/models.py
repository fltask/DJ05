from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    
    # Используем username как поле для входа (по умолчанию)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
