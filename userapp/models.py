from unittest.util import _MAX_LENGTH
from django.db import models

class username(models.Model):
    username=models.CharField(max_length = 30)