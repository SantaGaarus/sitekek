from django.db import models

class photososi(models.Model):
    image = models.ImageField(upload_to='mebel/images/')
