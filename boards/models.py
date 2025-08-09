from django.db import models


class MessageBoard(models.Model):
    """A message"""
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

