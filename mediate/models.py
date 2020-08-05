from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)  # Update to use forms.
    created_at = models.DateTimeField(auto_now_add=True)
