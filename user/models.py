from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # related_name qo‘shildi
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # related_name qo‘shildi
        blank=True
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username", "email"]

    def __str__(self):
        return self.phone_number
