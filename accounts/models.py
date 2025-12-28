from django.contrib.auth.models import User
from django.db import models

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name
