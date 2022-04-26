from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
	#is_dtag = models.BooleanField(default=True)