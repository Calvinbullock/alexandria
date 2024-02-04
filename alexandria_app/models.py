from django.db import models
# from django.core.files.base import BaseStorage
import os
# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='file/')

"""
class LocalStorage(BaseStorage):
    def __init__(self, location):
        self.location = location

    def url(self, name):
        return os.path.join(self.location, name)

    def open(self, name, mode='rb'):
        full_path = os.path.join(self.location, name)
        return open(full_path, mode)

    # Implement other methods like exists, delete, etc.
"""
