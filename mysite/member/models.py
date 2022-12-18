from django.db import models


class Member(models.Model):
    user_id = models.CharField(primary_key=True, max_length=40, null=False, blank=False)
    user_name = models.CharField(max_length=40, null=False, blank=False)
    user_pass = models.CharField(max_length=40, null=False, blank=False)
    tel = models.CharField(max_length=40, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)

